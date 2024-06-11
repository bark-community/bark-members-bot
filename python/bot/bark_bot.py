import logging
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from bot.commands import (
    start, help_command, balance, topup, payment, swap, donate, referral, bonus, airdrop, 
    nft_info, membership_info, governance_info, qr_payment
)
from utils.helpers import get_wallet_info

class BARKBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.init_commands()

    def init_commands(self):
        self.dispatcher.add_handler(CommandHandler("start", start))
        self.dispatcher.add_handler(CommandHandler("help", help_command))
        self.dispatcher.add_handler(CommandHandler("balance", balance))
        self.dispatcher.add_handler(CommandHandler("topup", topup))
        self.dispatcher.add_handler(CommandHandler("payment", payment))
        self.dispatcher.add_handler(CommandHandler("swap", swap))
        self.dispatcher.add_handler(CommandHandler("donate", donate))
        self.dispatcher.add_handler(CommandHandler("referral", referral))
        self.dispatcher.add_handler(CommandHandler("bonus", bonus))
        self.dispatcher.add_handler(CommandHandler("airdrop", airdrop))
        self.dispatcher.add_handler(CommandHandler("nft_info", nft_info))
        self.dispatcher.add_handler(CommandHandler("membership_info", membership_info))
        self.dispatcher.add_handler(CommandHandler("governance_info", governance_info))
        self.dispatcher.add_handler(CommandHandler("qr_payment", qr_payment))
        # Add more command handlers as needed

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
