import sys
import csv

with open(sys.argv[1], encoding="utf-8") as csv_:
    reader = csv.reader(csv_)
    obsah = list(reader)
    print(obsah)

