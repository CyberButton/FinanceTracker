# import numpy as np
import sqlite3
# import pandas as pd
from datetime import date

# GOODS_OR_SERVICES = []
# PRICES = []
# DATES = []
# EXPENSE_TYPES = []


# def add_expense(goods_or_services, price, date, expense_type):
#     GOODS_OR_SERVICES.append(goods_or_services)
#     PRICES.append(price)
#     DATES.append(date)
#     EXPENSE_TYPES.append(expense_type)

def get_info():
    with connection:
        crsr.execute("SELECT * FROM expenses")
        print(crsr.fetchall())


option = -1
expense_type = ""

# connecting to the databsae
connection = sqlite3.connect("expenses.db")

# cursor
crsr = connection.cursor()

# sql_command = """CREATE TABLE expenses (
# Goods or Services VARCHAR(35),
# prices VARCHAR(30),
# dates DATE,
# expense types VARCHAR(30));"""

# execute the statement

crsr.execute("CREATE TABLE IF NOT EXISTS expenses (Goods_or_Services VARCHAR(35), prices VARCHAR(10), dates VARCHAR("
             "15), expense_types VARCHAR(30));")
# crsr.execute("CREATE TABLE movie(title, year, score)")
while option != 0:
    print("Welcome user, to this simple expense tracker:")
    print("1. Add Food Expense")
    print("2. Add Entertainment Expense")
    print("3. Add Other Expense")
    print("4. Show and Save the Expense Report")
    print("0. Exit")
    option = int(input("Choose an option:\n"))

    print("")

    if option == 0:
        # close the connection
        connection.close()
        print("Exiting the program")
        break
    elif option == 1:
        print("Adding Food")
        expense_type = "FOOD"
    elif option == 2:
        print("Adding Entertainment cost")
        expense_type = "ENTERTAINMENT"
    elif option == 3:
        print("Adding Other")
        expense_type = "OTHER"
    elif option == 4:

        get_info()

        # expense_report = pd.DataFrame()
        # expense_report["GOODS_OR_SERVICES"] = GOODS_OR_SERVICES
        # expense_report["PRICES"] = PRICES
        # expense_report["DATES"] = DATES
        # expense_report["EXPENSE TYPES"] = EXPENSE_TYPES

        # expense_report.to_csv("expenses.csv")

        # print(expense_report)
    else:
        print("PLEASE SELECT ONLY OPTIONS 0, 1, 2, 3, 4")

    if option == 1 or option == 2 or option == 3:
        goods_or_services = input("Give specific name of your spending in category " + expense_type + ":\n")
        price = input("Money spent:\n")
        today = date.today()
        # add_expense(goods_or_services, price, today, expense_type)
        crsr.execute("INSERT INTO expenses (Goods_or_Services, prices, dates, expense_types) VALUES(?, ?, ?, ?)", (goods_or_services, price, today, expense_type))
        connection.commit()
        print()
