import pytest
from utils.api_client import APIClient
from resources.test_data import *


@pytest.mark.parametrize("auth_token, expected_status", auth_test_cases)
def test_transaction_authentication(auth_token, expected_status, wallet_id=wallet_id, payload=payloads_to_verify_response):
    response = APIClient.post_transaction(wallet_id, payload)
    assert response.status_code == expected_status
