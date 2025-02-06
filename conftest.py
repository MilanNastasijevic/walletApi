import pytest
from resources import config, payloads

@pytest.fixture
def headers():
    return {
        "Authorization": f"Bearer {config.AUTH_TOKEN}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def valid_payload():
    return payloads.valid_transaction_payload()
