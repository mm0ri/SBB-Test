import csv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

main_l = []

#with open('d:/User Projects/SBB-Test/src/binlist-data.csv', 'r') as csv_file:
with open('d:/User Projects/SBB-Test/src/binlist-data.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        main_l.append(row)

for row in main_l:
    print(row)