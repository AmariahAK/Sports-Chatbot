
```markdown
# Sports Chatbot with Flask and Twilio

A chatbot that provides real-time sports updates, game highlights, and betting links via WhatsApp, Telegram, and SMS. Users can navigate through leagues, teams, and games with an intuitive interface, similar to MPesa's prompt-based system. Built with Flask and integrated with the SportMonks API.

---

## Features
- **View Highlights**: Users can view highlights of past games.
- **Today’s Games**: Navigate through ongoing leagues, teams, and game details.
- **Betting Links**: Users can choose a game and receive a direct link to Betika.
- **Intuitive Navigation**: Includes `Back`, `Home`, and `Exit` options for smooth user experience.
- **Accessible on WhatsApp, Telegram, and SMS**: Powered by Twilio's messaging API.

---

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.10+
- Pip
- A Twilio account
- A SportMonks API key

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sports-chatbot.git
   cd sports-chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/macOS
   venv\Scripts\activate       # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add the following:
     ```
     SPORTMONKS_API_KEY=your_sportmonks_api_key
     TWILIO_ACCOUNT_SID=your_twilio_account_sid
     TWILIO_AUTH_TOKEN=your_twilio_auth_token
     TWILIO_PHONE_NUMBER=your_twilio_phone_number
     ```
   - Replace placeholders with your actual API keys and credentials.

5. Initialize the Flask application:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

---

## Running the Project

1. Start the Flask server:
   ```bash
   flask run
   ```

2. Expose the Flask app to the internet using a tunneling tool like **ngrok**:
   ```bash
   ngrok http 5000
   ```
   - Copy the public URL provided by ngrok (e.g., `https://abc123.ngrok.io`).

3. Set the ngrok URL as your Twilio webhook:
   - Log in to your Twilio account.
   - Navigate to **Messaging > Webhooks**.
   - Set the URL to `https://abc123.ngrok.io/webhook`.

---

## Project Structure

```plaintext
.
├── README.md
├── app.py
├── bot
│   ├── __init__.py
│   ├── sportmonks_api.py
│   └── twilio_webhook.py
├── config
│   ├── __init__.py
│   └── config.py
├── migrations
├── requirements.txt
└── .env
```

---

## APIs Used
- **[SportMonks API](https://www.sportmonks.com/)**: Fetch leagues, teams, and game details.
- **[Twilio Messaging API](https://www.twilio.com/messaging)**: Send and receive messages via WhatsApp, Telegram, and SMS.

---

## Navigation Flow

1. **Main Menu**:
   - 1: View Highlights
   - 2: View Today’s Games

2. **Today’s Games**:
   - Choose a league (ongoing leagues only).
   - Choose a team.
   - View game details and receive betting links.

3. **Navigation Options**:
   - `Back`: Return to the previous menu.
   - `Home`: Return to the main menu.
   - `Exit`: End the session.

---

## Deployment
### Recommended Hosting Platforms
1. **AWS Elastic Beanstalk**  
2. **Heroku**  
3. **Google Cloud Run**  
4. **DigitalOcean App Platform**

---

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, open an issue first to discuss what you'd like to change.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any inquiries or support, please contact:
- **Email**: [amariah.abish@gmail.com](mailto:amariah.abish@gmail.com)
- **Phone**: 0720151950
```
