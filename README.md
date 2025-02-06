# Wallet API Test Framework 

##  Overview
This is a **pytest-based automation framework** focused mainly on testing the `/wallet/{walletId}/transaction` API.


##  Setup & Installation
### STEP 1 Install Dependencies
```sh
pip install -r requirements.txt
```
### STEP 2 Run Tests
```sh
To run complete test suit
pytest -v

For individual test run
pytest ./tests/test_transactions.py(MAC OS)

NOTE: For Windows OS, slightly different path parameter for command line may need. Like 
.\tests\test_transactions.py 
Not having resource atm.
```
