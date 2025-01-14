import requests
from config import config

BASE_URL = "https://api.sportmonks.com/v3/"
API_KEY = config["SPORTMONKS_API_KEY"]

def get_ongoing_leagues():
    """Fetch ongoing leagues."""
    url = f"{BASE_URL}/leagues?api_token={API_KEY}&filter[status]=active"
    response = requests.get(url)
    leagues = response.json().get("data", [])
    return [league["name"] for league in leagues]

def get_teams_by_league(league_name):
    """Fetch teams in a given league."""
    url = f"{BASE_URL}/teams?api_token={API_KEY}&filter[league]={league_name}"
    response = requests.get(url)
    teams = response.json().get("data", [])
    return [team["name"] for team in teams]

def get_games_by_league(league_name, team=None):
    """Fetch games by league or specific team."""
    url = f"{BASE_URL}/fixtures?api_token={API_KEY}&filter[league]={league_name}"
    if team:
        url += f"&filter[team]={team}"
    response = requests.get(url)
    games = response.json().get("data", [])
    return [f"{game['home_team']} vs {game['away_team']} at {game['time']}" for game in games]
