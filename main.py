from func import *
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

res_list = file_init()

app = FastAPI()

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
    return data_check(card_init(str(card_number)), res_list,)


