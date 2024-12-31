import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    FORCE_SUB_CHANNELS = os.environ.get("FORCE_SUB_CHANNELS", "").split("-1002135593873,-1001764441595")  # Add multiple channel IDs separated by commas


