from datetime import datetime

date_format= "%d-%m-%Y"
#created A Dictionary here to Keep track of Categories User is putting
Categories={"I": "Income", "E":"Expense"}

def get_date(prompt,allow_default=False):
    date_str=input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        return get_date(prompt, allow_default)
    

def get_amount():
    try:
        amount = float(input("Enter the amount:"))
        if amount<=0:
            return ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
                             
def get_category():
    category= input("Enter the catergory ('I' for Income or 'E'for Expense): ").upper()
    if category in Categories:
        return Categories[category]
    print(" Invalid Category. Please enter 'I' for income or 'E' for expense. ")
def get_description():
    return input("Enter a description: ")
