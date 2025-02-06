import pytest

import resources.payloads
from helpers.assertion import *
from resources.test_data import payloads_to_verify_response,wallet_id
from utils.api_client import APIClient
from resources.test_data import transaction_test_cases, wallet_id_test_cases


@pytest.mark.parametrize("amount, transaction_type, currency, expected_status", transaction_test_cases)
def test_transaction_variants(amount, transaction_type, currency, expected_status, expected_keys):
    payload = resources.payloads.valid_transaction_payload(amount, transaction_type, currency)
    response = APIClient.post_transaction(wallet_id, payload)
    valid_response_assertion(response, expected_status, payloads_to_verify_response)


@pytest.mark.parametrize("wallet_id, expected_status", wallet_id_test_cases)
def test_transaction_with_various_wallet_ids(wallet_id, expected_status):
    payload = {
        "amount": 100.0,
        "type": "credit",
        "description": "Wallet ID Test",
        "currency": "USD"
    }
    response = APIClient.post_transaction(wallet_id, payload)
    explanatory_assertion(response, expected_status)
