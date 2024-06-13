import requests
from config.settings import CNFT_API_URL

def check_cnft_token(wallet_address, token_id):
    response = requests.get(f"{CNFT_API_URL}/address/{wallet_address}/tokens")
    tokens = response.json().get('tokens', [])
    return any(token['tokenId'] == token_id for token in tokens)
