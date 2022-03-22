from func import *
from fastapi import FastAPI

app = FastAPI()

res_list = file_init()

@app.get("/", status_code=200)
async def start_page():
    return "Please, make response by using parametr /cards/'bank card number'"

@app.get("/cards/", status_code=200)
async def card_page():
    return "Card number should have size more than 16 and less than 20 digits. Also its should contain only numbers withous free space."

@app.get("/cards/{card_number}", status_code=200)
async def read_item(card_number):
    return data_check(card_init(card_number), res_list,)
