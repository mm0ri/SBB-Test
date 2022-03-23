import unittest
import requests
from fastapi import HTTPException
from func import *

main_l = file_init()

class TestBank(unittest.TestCase):

    def test_card(self):
        self.assertEqual(card_init('51890120000000000000'), '518901')
        self.assertEqual(card_init('11110011111111111111'), '111100')

    def test_logic(self):
        self.assertEqual(data_check('518901', main_l), ['518901','MASTERCARD','CREDIT','GOLD','TINKOFF CREDIT SYSTEMS BANK (CJSC)','RU','RUS','RUSSIA','61.524','105.319',"",'www.tinkoff.ru/eng/'])
        self.assertEqual(data_check('402311', main_l), ['402311','VISA','DEBIT','CLASSIC','AKB INVESTSBERBANK CB OF INVESTMENTS ANDSAVINGS','RU','RUS','RUSSIA','61.524','105.319',"",""])
        self.assertEqual(data_check('676280', main_l), ['676280','MAESTRO','DEBIT',"",'SBERBANK OF RUSSIA','RU','RUS','RUSSIA','61.524','105.319','+7 (495) 500-5550','www.sberbank.com'])
        self.assertEqual(data_check('341142', main_l), ['341142','AMERICAN EXPRESS','CREDIT',"",'AMERICAN EXPRESS','US','USA','United States','37.0902','-95.7129','1-800-528-4800','www.americanexpress.com'])

    def test_responses(self):
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/40231120000000000000').status_code, 200)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/51890120000000000000').status_code, 200)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/11110011111111111111').status_code, 200)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/111100111111111111111').status_code, 500)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/11110011').status_code, 500)
        self.assertEqual(requests.get('http://127.0.0.1:8000/cards/000000000000000000000').status_code, 500)
