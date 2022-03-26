from func import *
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse, FileResponse

res_list = file_init()

app = FastAPI()
favicon_path = 'favicon.ico'

@app.exception_handler(404)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/",)

@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)

@app.get("/", status_code=200, response_class=PlainTextResponse)
async def start_page():
    return "Please, make right request. Just add this after ip: /cards/'bank card number'\nTo get more information move to: '/cards/'."

@app.get("/cards/", status_code=200, response_class=PlainTextResponse)
async def card_page():
    return "Please, make right request. Just add this after ip: /cards/'bank card number'.\nRules:\nCard number should have size greater than or equal to 16 and less than or equal to 20 digits.\nAlso its should contain only numbers withous any free space."

@app.get("/cards/{card_number}", status_code=200)
async def read_item(card_number):
    return data_check(card_init(str(card_number)), res_list,)
    