"""
DevLog ID Generator Script

Generates a unique development ID for tagging code and notes.
Stores ID history in a JSON file and resets daily.

Command  to copy paste in terminal : 

python dev_log_id_gen.py

"""

from datetime import datetime, timedelta
import json
import os

# Path to the JSON log file
LOG_FILE_PATH = "devlog_log.json"

# Load existing history or start a new one
if os.path.exists(LOG_FILE_PATH):
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
        history = json.load(file)
else:
    history = {}

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

# Count today's entries
history[today] = history.get(today, 0) + 1

# Format the new DevLog ID
entry_number = str(history[today]).zfill(2)
DEVLOG_ID = f"DEV-{today}-{entry_number}"

# Keep only the last 30 days
cutoff = datetime.now() - timedelta(days=30)
history = {
    date: count for date, count in history.items()
    if date >= cutoff.strftime("%Y-%m-%d")}

# Save updated history
with open(LOG_FILE_PATH, "w", encoding="utf-8") as file:
    json.dump(history, file, indent=2)

# Output the DevLog ID with spacing for visibility
print("\n" + DEVLOG_ID + "\n")
