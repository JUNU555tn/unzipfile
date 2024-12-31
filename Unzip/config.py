import os
import re

# Define the ID pattern for channel IDs (allowing negative values for IDs)
id_pattern = re.compile(r'^-?\d+$')  # Allow negative numbers for channel IDs

# Directly assign the AUTH_CHANNEL values here
AUTH_CHANNEL = [-1001764441595, -1002135593873]

class config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    
    # Directly set AUTH_CHANNEL from the list above
    AUTH_CHANNEL = AUTH_CHANNEL

# Print AUTH_CHANNEL to verify it's set correctly
print("AUTH_CHANNEL:", config.AUTH_CHANNEL)
