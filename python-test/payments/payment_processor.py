import stripe

stripe.api_key = os.getenv("STRIPE_API_KEY")

def process_payment(amount, currency, payment_method):
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            confirmation_method='manual',
            confirm=True,
        )
        return intent
    except Exception as e:
        print(f"Error processing payment: {e}")
        return None
