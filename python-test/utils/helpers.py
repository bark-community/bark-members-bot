import qrcode
from io import BytesIO
from PIL import Image

def get_wallet_info(user_id):
    # Dummy data for wallet info
    return {
        "user_id": user_id,
        "balance": 1000,  # Example balance
        "transaction_history": []
    }

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    return buffered
