def valid_transaction_payload(amount, transaction_type, currency):
    return {
        "amount": amount,
        "type": transaction_type,
        "description": "Automated Test Transaction",
        "currency": currency
    }
