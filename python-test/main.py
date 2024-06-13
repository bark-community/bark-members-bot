import os
from dotenv import load_dotenv
from bot import BARKBot

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Initialize the BARK Bot
    bot = BARKBot()
    bot.run()
