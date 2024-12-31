import os
import re

# Define the ID pattern for channel IDs
id_pattern = re.compile(r'^.\d+$')

# Get the AUTH_CHANNEL environment variable and process it
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in os.environ.get('AUTH_CHANNEL', '').split()]  # Space-separated channel IDs

class config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    
    # You can access AUTH_CHANNEL directly from here if needed
    AUTH_CHANNEL = AUTH_CHANNEL
