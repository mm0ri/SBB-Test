import csv
from pathlib import Path
import os

home = os.getcwd()
path_to_file = Path(home,"app", "binlist-data.csv")
print(path_to_file)

def file_init():
    main_l = []
    with open(path_to_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            main_l.append(row)
        return print('ok')
        
file_init()

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))