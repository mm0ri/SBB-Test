from func import *
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.responses import RedirectResponse

# To start tests use command: pytest test_check.py

app = FastAPI()

res_list = file_init()

@app.exception_handler(404)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/",)

@app.get("/", status_code=200)
async def start_page():
    return "Please, make response by using parametr /cards/'bank card number'"

@app.get("/cards/", status_code=200)
async def card_page():
    return "Card number should have size more than 16 and less than 20 digits. Also its should contain only numbers withous free space."

@app.get("/cards/{card_number}", status_code=200)
async def read_item(card_number):
    return data_check(card_init(card_number), res_list,)

client = TestClient(app)

def test_start_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Please, make response by using parametr /cards/'bank card number'"

def test_card_page():
    response = client.get("/cards/")
    assert response.status_code == 200
    assert response.json() == "Card number should have size more than 16 and less than 20 digits. Also its should contain only numbers withous free space."

def test_func_true():
    response = client.get("/cards/51890120000000000000")
    assert response.status_code == 200

def test_func_false():
    response = client.get("/cards/518901200000000000000")
    assert response.status_code == 500

def test_func_false2():
    response = client.get("/cards/5189012")
    assert response.status_code == 500

def test_exception():
    response = client.get("///")
    assert response.status_code == 200