import requests


def explanatory_assertion(response, expected_status):
    assert response.status_code == expected_status, (
        print(f'Expected {expected_status}, but got {response.status_code}. Response: {response.text}'))


def valid_response_assertion(response, expected_status, expected_keys):
    explanatory_assertion(response, expected_status) # reusing custom_assert to prevent unnecessary check

    json_data = response.json()
    for key, value in expected_keys.items():
        assert key in json_data, print(f"Key '{key}' is missing in response: {json_data}")
        assert json_data[key] == value, (
            print(f"Expected '{json_data[key]}' to be '{value}', but got '{key}'. "
                  f"Response: {json_data}")
        )

#TODO: data_type_validator to be included as separate method/function


def handling_exception(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Request successful")
    except requests.exceptions.RequestException as e:
        print("Request failed:", str(e))
