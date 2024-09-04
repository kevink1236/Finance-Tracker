import csv
import gspread
import time

MONTH = 'august'

file = f"2024_{MONTH}.csv"


transactions = []
sum = 0

def Fin2024(file):
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[2]
            amount = float(row[3])
            name = row[4]
            category = 'other'
            if ('CW' and 'JUNGHYUN PARK') in name and amount > 0:
                category = 'Allowance'
            elif ('CW' and 'YE WOON JUNG') in name and amount <= -1000:
                category = 'Rent'
            elif 'CW' in name:
                category = 'E-Transfer'
            elif 'OR' in name and amount > 0:
                category = 'Refund'
            elif 'OP' in name:
                category = 'Online Purchase'
            elif 'IB' in name:
                category = 'Internet Banking'
            elif 'PR' in name:
                category = 'In-store Purchase'
            transaction = ((date, name, amount, category))
            transactions.append(transaction)

        return transactions

gc = gspread.service_account()
sh = gc.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = Fin2024(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[2], row[3]], 7)
    time.sleep(2)
