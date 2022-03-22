from fastapi import HTTPException
import csv

path_to_file = 'd:/User Projects/SBB-Test/src/binlist-data.csv'

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
    else:
        status_code = 500
        raise HTTPException(status_code=500, detail=f'Status code: {status_code}. Wrong card number. Its size should be more that 16 and less that 20 digits and contains only numbers')

def data_check(n_card_number, main_l):
    for row in main_l:
        if row[0] == n_card_number:
            return(row)