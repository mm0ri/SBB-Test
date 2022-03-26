import unittest
import requests

# To start tests use this command: python3 -m unittest

class TestBank(unittest.TestCase):

    # Requests test

    def test_responses(self):

        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/40231120000000000000').status_code, 200) # fine simple request test
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/51890120000000000000').status_code, 200) # fine simple request test
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/11110011111111111111').status_code, 200) # fine simple request test
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/00000000000000000000').status_code, 500) # wrong card number check (card not in db)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/aaaaaaaaaaaaaaaaaa').status_code, 500) # wrong card type

        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/11110000000000000').status_code, 200) # card number size test (17 digits)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/111100111111111111111').status_code, 500) # card number size test (> 20)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/11110011').status_code, 500) # card number size test (< 16)

        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/').status_code, 200) # /cards/ page test (code 200 because redirect successfull)
        self.assertEqual(requests.get('http://127.0.0.1:8000////').status_code, 200) # Redirect check
        self.assertEqual(requests.get('http://127.0.0.1:8000/cad/').status_code, 200) # Redirect check 2