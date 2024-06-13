from solana.publickey import PublicKey
from solana.rpc.api import Client
from config.settings import SOLANA_RPC_URL

solana_client = Client(SOLANA_RPC_URL)

def check_bark_payment(user_wallet, amount, token_address):
    balance = solana_client.get_token_accounts_by_owner(PublicKey(user_wallet), PublicKey(token_address))
    if balance['result']['value'][0]['account']['data']['parsed']['info']['tokenAmount']['uiAmount'] >= amount:
        return True
    return False
