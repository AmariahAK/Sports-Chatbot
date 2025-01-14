from flask import Flask, request, jsonify
from bot.twilio_webhook import handle_incoming_message

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    """Handles incoming messages from Twilio."""
    incoming_data = request.json
    response = handle_incoming_message(incoming_data)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
