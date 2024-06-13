from telegram import Update
from telegram.ext import CallbackContext
from utils.solana_utils import check_sol_payment
from utils.bark_utils import check_bark_payment
from utils.cnft_utils import check_cnft_token
from config.settings import (
    SOL_WALLET_ADDRESS,
    BARK_WALLET_ADDRESS,
    SOL_PAYMENT_AMOUNT,
    BARK_PAYMENT_AMOUNT,
    CNFT_PROSPECT_TIER_TOKEN,
    CNFT_FULL_MEMBER_TIER_TOKEN,
    CNFT_VETERAN_MEMBER_TIER_TOKEN,
    CNFT_SOLDIER_TIER_TOKEN
)

def join_group(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_wallet = update.message.text.split()[1]  # Assuming the user sends their wallet address after the command
    
    if check_sol_payment(user_wallet, SOL_PAYMENT_AMOUNT):
        context.bot.send_message(chat_id=user_id, text="SOL payment received. Welcome to the group!")
        context.bot.add_chat_members(chat_id='THE_PEAKY_BARKERS_CLUB_CHAT_ID', user_ids=[user_id])
    elif check_bark_payment(user_wallet, BARK_PAYMENT_AMOUNT, BARK_WALLET_ADDRESS):
        context.bot.send_message(chat_id=user_id, text="BARK payment received. Welcome to the group!")
        context.bot.add_chat_members(chat_id='THE_PEAKY_BARKERS_CHAT_ID', user_ids=[user_id])
    elif check_cnft_token(user_wallet, CNFT_PROSPECT_TIER_TOKEN):
        context.bot.send_message(chat_id=user_id, text="CNFT Prospect Tier token detected. Welcome to the Prospect group!")
        context.bot.add_chat_members(chat_id='BARKERS_PROSPECT_GROUP_CHAT_ID', user_ids=[user_id])
    elif check_cnft_token(user_wallet, CNFT_FULL_MEMBER_TIER_TOKEN):
        context.bot.send_message(chat_id=user_id, text="CNFT Full Member Tier token detected. Welcome to the Full Member group!")
        context.bot.add_chat_members(chat_id='BARKERS_FULL_MEMBER_GROUP_CHAT_ID', user_ids=[user_id])
    elif check_cnft_token(user_wallet, CNFT_VETERAN_MEMBER_TIER_TOKEN):
        context.bot.send_message(chat_id=user_id, text="CNFT Veteran Member Tier token detected. Welcome to the Veteran group!")
        context.bot.add_chat_members(chat_id='BARKERS_VETERAN_GROUP_CHAT_ID', user_ids=[user_id])
    elif check_cnft_token(user_wallet, CNFT_SOLDIER_TIER_TOKEN):
        context.bot.send_message(chat_id=user_id, text="CNFT Soldier Tier token detected. Welcome to the Soldier group!")
        context.bot.add_chat_members(chat_id='BARKERS_SOLDIER_GROUP_CHAT_ID', user_ids=[user_id])
    else:
        context.bot.send_message(chat_id=user_id, text="Payment or CNFT token not detected. Please try again.")
