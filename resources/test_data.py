from resources import config

transaction_test_cases = [
    (100.0, "cc", "USD", 201), #TC01 Successful credit transaction
    (50.5, "dc", "EUR", 201), #TC02 Successful debit transaction
    (-10.0, "cc", "USD", 400), #TC04 Negative transaction amount
    (1e10, "cc", "USD", 400), #TC11 Large transaction amount
    (0, "cc", "USD", 400), #TC05 Zero amount transaction
    (101.0, "non-existing", "USD", 400), #TC06 Invalid transaction type
    (102.0, "cc", "INV", 400), #TC07 Unsupported currency
    (103.0, "cc", "", 400), #TC03 Missing required fields

]

wallet_id = "11A2245XC"
spec_char = "!@#$%^"

wallet_id_test_cases = [
    (wallet_id, 201),
    ("non_existing_wallet", 404),
    ("", 400),
    (spec_char, 400),
]

auth_test_cases = [
    (config.AUTH_TOKEN, 201),
    ("", 401),
    (config.INVALID_AUTH_TOKEN, 403), #TC10 Invalid authentication token
]

# instead of having method to create for hypothetical user for e-wallet API
# and on login action to access user profile and collect walletId,
# have store a hardcoded value inside variable for reference through code

payloads_to_verify_response = {
    "amount": 1,
    "type": "debit",
    "description": "Automated Test Transaction",
    "currency": "RSD"
}
#

