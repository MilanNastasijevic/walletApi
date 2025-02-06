import threading
from utils.api_client import APIClient
from resources.test_data import wallet_id


def transaction_send(wallet_id, amount, currency_type):
    payload = {
        "amount": amount,
        "type": "cc",
        "description": "Concurrent Test",
        "currency": currency_type
    }
    return APIClient.post_transaction(wallet_id, payload)


# TC13 Concurrent transactions handling
def test_concurrent_transactions(wallet_Id=wallet_id):

    transactions_num = 5
    threads = []
    results = []

    for i in range(transactions_num):
        currency_type = "USD" if i % 2 == 0 else "EUR"
        thread = threading.Thread(target=lambda: results.append(
            transaction_send(wallet_Id, 10.0, currency_type)
        ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for response in results:
        assert response.status_code in [201, 400]
