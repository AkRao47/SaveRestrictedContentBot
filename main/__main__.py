

import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from main import bot
from flask import Flask

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# Create a Flask app
app = Flask(__name__)

# Don't be a thief
print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

if __name__ == "__main__":
    bot.start()  # Assuming 'start' is the method to start the bot in your 'bot' instance
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
