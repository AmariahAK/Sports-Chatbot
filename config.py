import os

class Config:
    SPORTMONKS_API_KEY = os.getenv("SPORTMONKS_API_KEY", "your_sportmonks_api_key")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_twilio_account_sid")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_twilio_auth_token")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "your_twilio_phone_number")
    BETIKA_URL = "https://www.betika.com/"

config = Config()
