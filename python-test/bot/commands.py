from telegram import Update
from telegram.ext import CallbackContext
from utils.helpers import get_wallet_info, generate_qr_code
from nfts.nft_manager import get_nft_info
from membership.membership_tiers import get_membership_info
from governance.governance import get_governance_info

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to BARK Bot!")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
/start - Start new dialog
/help - Show commands
/balance - Show balance
/topup - Add credits to your account
/payment - Process a payment
/swap - Swap tokens
/donate - Make a donation
/referral - Get your referral link
/bonus - Claim your bonus
/airdrop - Claim an airdrop
/nft_info - Get NFT information
/membership_info - Get membership tier information
/governance_info - Get governance information
/qr_payment - Make a payment via QR code
""")

def balance(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    balance_info = get_wallet_info(user_id)
    update.message.reply_text(f"Your balance is: {balance_info['balance']} BARK Tokens")

def topup(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Top-up functionality coming soon!")

def payment(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Payment functionality coming soon!")

def swap(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Swap functionality coming soon!")

def donate(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Donate functionality coming soon!")

def referral(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Referral functionality coming soon!")

def bonus(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bonus functionality coming soon!")

def airdrop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Airdrop functionality coming soon!")

def nft_info(update: Update, context: CallbackContext) -> None:
    nft_info = get_nft_info()
    update.message.reply_text(f"NFT Info: {nft_info}")

def membership_info(update: Update, context: CallbackContext) -> None:
    membership_info = get_membership_info()
    update.message.reply_text(f"Membership Info: {membership_info}")

def governance_info(update: Update, context: CallbackContext) -> None:
    governance_info = get_governance_info()
    update.message.reply_text(f"Governance Info: {governance_info}")

def qr_payment(update: Update, context: CallbackContext) -> None:
    qr_code = generate_qr_code("Payment Details")
    update.message.reply_photo(qr_code, caption="Scan this QR code to make a payment")
