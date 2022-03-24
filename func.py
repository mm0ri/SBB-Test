import csv
import os

from fastapi import HTTPException
from pathlib import Path

home = os.getcwd()
path_to_file = Path(home, "src", "binlist-data.csv") # Actually, should work, but Sometimes has problems with path.

#path_to_file = 'd:/User Projects/SBB-Test/src/binlist-data.csv' # If you have problems with path, you should use this line with your own path to src folder in project folder.

def file_init():
    main_l = []
    with open(path_to_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            main_l.append(row)
        return main_l

def card_init(card_number):
    if len(card_number) >= 16 and len(card_number) <= 20 and card_number.isdigit():
        n_card_number = card_number[0:6]
        return n_card_number
    elif card_number.isdigit() == False:
        status_code = 500
        raise HTTPException(status_code, detail=f'Status code: {status_code}. Wrong card number type. Its should contain only numbers.')
    elif len(card_number) < 16:
        status_code = 500
        raise HTTPException(status_code, detail=f'Status code: {status_code}. Wrong card number size. Its size should be greater than or equal to 16.')
    elif len(card_number) > 20:
        status_code = 500
        raise HTTPException(status_code, detail=f'Status code: {status_code}. Wrong card number size. Its size should be less than or equal to 20.')
    else:
        status_code = 500
        raise HTTPException(status_code, detail=f'Status code: {status_code}. Wrong card number. Its size should be greater than or equal 16 and less than or equal to 20 digits and contain only numbers. And has no free space in the number')

def data_check(n_card_number, main_l):
    for row in main_l:
        if row[0] == n_card_number:
            return(row)
    else:
        raise HTTPException(status_code = 500, detail='Card not in database.')