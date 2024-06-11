# bark-bot/bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
from config import settings
from bark_bot.commands import *

class BARKBot:
    def __init__(self):
        self.application = ApplicationBuilder().token(settings['telegram']['token']).build()

        self.application.add_handler(CommandHandler("start", start))
        self.application.add_handler(CommandHandler("balance", balance))
        self.application.add_handler(CommandHandler("topup", topup))
        self.application.add_handler(CommandHandler("settings", settings_command))
        self.application.add_handler(CommandHandler("help", help_command))
        self.application.add_handler(CommandHandler("role", role))
        self.application.add_handler(CommandHandler("model", model))
        self.application.add_handler(CommandHandler("admin", admin_command))
        self.application.add_handler(CommandHandler("donate", donate))
        self.application.add_handler(CommandHandler("payments", payments))
        self.application.add_handler(CommandHandler("swap", swap))

    def run(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.application.run_polling()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to BARK BOT! Type /help to see available commands.")
