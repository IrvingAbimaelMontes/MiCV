import os

class StripeConfig:
    """Configuración para Stripe"""
    
    # Claves de API de Stripe
    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'pk_test_your_public_key')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_your_secret_key')
    STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET', 'whsec_your_webhook_secret')
    
    # Configuración de productos
    PRODUCTS = {
        'premium_template': {
            'name': 'Plantillas Premium',
            'description': 'Acceso a plantillas premium de CV',
            'price': 999,  # $9.99 en centavos
            'currency': 'usd'
        }
    }
    
    # Configuración de webhooks
    WEBHOOK_EVENTS = [
        'checkout.session.completed',
        'payment_intent.succeeded',
        'payment_intent.payment_failed'
    ]
    
    # Configuración de checkout
    CHECKOUT_CONFIG = {
        'payment_method_types': ['card'],
        'mode': 'payment',
        'billing_address_collection': 'auto',
        'shipping_address_collection': {
            'allowed_countries': ['US', 'CA', 'MX', 'ES', 'FR', 'DE', 'IT', 'GB']
        }
    }
