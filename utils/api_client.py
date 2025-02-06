import requests
from resources import config

class APIClient:
    @staticmethod
    def post_transaction(wallet_id, payload):
        headers = {
            "Authorization": config.AUTH_TOKEN,
            "Content-Type": "application/json"
        }
        response = requests.post(f"{config.BASE_URL}/{wallet_id}/transaction", json=payload, headers=headers)
        return response
