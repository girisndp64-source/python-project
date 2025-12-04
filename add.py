import csv
import pandas as pd

def add_entry():
    file = pd.read_csv('data.csv')
    file.columns = file.columns.str.lower()
    day = file['day'].iloc[-1] + 1
    with open('data.csv', 'a', newline="") as d:
      writer = csv.writer(d)
      temp = float(input("Enter the temperature (°C): "))
      rainfall = float(input("Enter the rainfall (mm): "))
      writer.writerow([day, temp, rainfall])
      again = input("You want to add another day?, press 'y' for yes or 'n' for no: ")
    if "y" in again.lower():
            add_entry()
    else:
            print("Data entry complete.")

add_entry()

        



