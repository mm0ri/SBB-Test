from func import *
from fastapi import FastAPI

app = FastAPI()

res_list = file_init()

@app.get("/cards/{card_number}", status_code=200)
async def read_item(card_number):
    return data_check(card_init(card_number), res_list,)
