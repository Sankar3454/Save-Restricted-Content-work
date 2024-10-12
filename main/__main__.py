import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot
from flask import Flask
import os
from threading import Thread

# Setup logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Load plugins
path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# Basic web server for port binding
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web_server():
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

# Don't be a thief 
print("Successfully deployed!")
print("By Akash Sodh • OTT Walla")

if __name__ == "__main__":
    # Start the web server in a separate thread
    Thread(target=run_web_server).start()
    
    # Start the bot
    bot.run_until_disconnected()
