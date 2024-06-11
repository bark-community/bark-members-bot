# main.py

from bark_bot.bot import BARKBot
from payments.server import app
import threading

def run_flask():
    app.run(debug=True)

def run_bot():
    bot = BARKBot()
    bot.run()

if __name__ == "__main__":
    # Run Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run Telegram bot
    run_bot()
