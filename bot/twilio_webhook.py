from bot.sportsmonks_api import get_ongoing_leagues, get_games_by_league, get_teams_by_league
from config import config

# User state management (replace with DB for production)
user_states = {}
user_choices = {}

def handle_incoming_message(data):
    """Process the incoming message and return a response."""
    message = data.get("Body", "").strip().lower()
    from_number = data.get("From", "")

    # Fetch user state and choices
    state = user_states.get(from_number, "default")
    user_data = user_choices.get(from_number, {})

    if message == "home":
        user_states[from_number] = "default"
        return {"Body": "Welcome back to the main menu.\n1. View Highlights\n2. View Today's Games\nType the number to choose."}

    if message == "back":
        # Go back to the previous state
        previous_state = user_data.get("previous_state", "default")
        user_states[from_number] = previous_state
        return handle_incoming_message({"Body": "state_return", "From": from_number})

    if state == "default":
        # Initial menu
        if message == "1":
            return {"Body": "Here are the latest highlights:\n1. Match 1 Highlight\n2. Match 2 Highlight\n..."}
        elif message == "2":
            user_states[from_number] = "choosing_league"
            leagues = get_ongoing_leagues()
            user_choices[from_number] = {"previous_state": "default"}
            return {"Body": "Choose a league:\n" + "\n".join(f"{i+1}. {league}" for i, league in enumerate(leagues)) + "\nType the number to choose or 'Home' to return."}
        else:
            return {"Body": "Invalid choice. Please type '1' or '2'."}

    elif state == "choosing_league":
        leagues = get_ongoing_leagues()
        try:
            selected_index = int(message) - 1
            selected_league = leagues[selected_index]
            user_states[from_number] = "choosing_team"
            user_choices[from_number] = {
                "previous_state": "choosing_league",
                "selected_league": selected_league
            }
            teams = get_teams_by_league(selected_league)
            return {"Body": f"You selected {selected_league}.\nChoose a team:\n" + "\n".join(f"{i+1}. {team}" for i, team in enumerate(teams)) + "\nType the number to choose or 'Back' to go back."}
        except (ValueError, IndexError):
            return {"Body": "Invalid choice. Please type the number of the league."}

    elif state == "choosing_team":
        selected_league = user_choices[from_number].get("selected_league")
        teams = get_teams_by_league(selected_league)
        try:
            selected_index = int(message) - 1
            selected_team = teams[selected_index]
            user_states[from_number] = "team_details"
            user_choices[from_number] = {
                "previous_state": "choosing_team",
                "selected_team": selected_team
            }
            games = get_games_by_league(selected_league, team=selected_team)
            return {"Body": f"You selected {selected_team}.\nGames:\n" + "\n".join(f"{i+1}. {game}" for i, game in enumerate(games)) + "\nType the number to choose a game, 'Back' to go back, or 'Home' to return."}
        except (ValueError, IndexError):
            return {"Body": "Invalid choice. Please type the number of the team."}

    elif state == "team_details":
        selected_team = user_choices[from_number].get("selected_team")
        try:
            # Simulate betting link for the selected game
            return {"Body": f"Game details for {selected_team}:\nClick here to bet: https://betika.com\nType 'Back' to go back or 'Home' to return."}
        except:
            return {"Body": "An error occurred. Please try again or type 'Home' to restart."}

    return {"Body": "Something went wrong. Please type 'Home' to restart."}
