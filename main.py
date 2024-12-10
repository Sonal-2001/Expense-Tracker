import pandas as pd
import csv
from datetime import datetime
from data_logging import get_amount, get_date, get_description, get_category
import matplotlib.pyplot as plt
class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]
    FORMAT = "%d-%m-%Y"

    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=CSV.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry= {
             "date":date,
             "amount":amount,
             "category":category,
             "description": description}
         
        with open(cls.CSV_FILE, 'a',newline="") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")
    
    @classmethod
    def get_transaction(cls,start_date,end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df["date"]= pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date=datetime.strptime(start_date,CSV.FORMAT)
        end_date=datetime.strptime(end_date,CSV.FORMAT)

        mask=(df["date"]>= start_date) & (df["date"]<=end_date)
        filtered_df= df.loc[mask]
        if filtered_df.empty:
            print("No transaction found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string( index=False, formatters={"date": lambda x:x.strftime(CSV.FORMAT)} ))

            total_income=filtered_df[filtered_df["category"]=="Income"]["amount"].sum()
            total_expence= filtered_df[filtered_df["category"]=="Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expence:.2f}")
            print(f"Net Saving: ${(total_income-total_expence):.2f}")
        return filtered_df


def add():
    CSV.initialize_csv()
    date=get_date("Enter the transaction date (dd-mm-yyyy) or Press Enter for today's date: ",allow_default=True)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)
def plot_transactions(df):
    df.set_index("date",inplace=True)
    
    income_df=(df[df["category"]=="Income"].resample("D").sum().reindex(df.index,fill_value=0))
    expense_df=(df[df["category"]=="Expense"].resample("D").sum().reindex(df.index,fill_value=0))
    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df["amount"],label="Income",color="b")
    plt.plot(expense_df.index, expense_df["amount"],label="Expense",color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    while True:
        print("\n1. Add Transaction")
        print("2. View Transaction and summary within a date range...")
        print("3. Exit")
        choice=input("Enter your choice:(1-3): ")
        if choice=="1":
            add()
        elif choice=="2":
            start_date=input("Enter the start date (dd-mm-yyyy): ")
            end_date=input("Enter the end date (dd-mm-yyyy): ")
            df=CSV.get_transaction(start_date, end_date)
            if input("Do you want to see a plot? (y/n)").lower() == "y":
                plot_transactions(df)
        elif choice=="3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()