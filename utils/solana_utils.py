from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.rpc.types import TxOpts
from solana.system_program import TransferParams, transfer
from config.settings import SOLANA_RPC_URL

solana_client = Client(SOLANA_RPC_URL)

def check_sol_payment(wallet_address, required_amount):
    balance = solana_client.get_balance(PublicKey(wallet_address))
    return balance['result']['value'] >= required_amount
