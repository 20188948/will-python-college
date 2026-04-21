import pandas as pd
import matplotlib.pyplot as plt

# Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- SportZone Sales Analysis Module ----------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Total sales by category")
        print('3. Income and profit made on products')

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            flag = True

    return int(choice)


# Generates submenu of available product codes and allows user to select a product to view
def get_product_id():

    df = pd.read_csv("/workspaces/codespaces-blank/Task4a_SportZone_data.csv")

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- SportZone Sales Analysis Module ----------- ")
        print("-"*66)
        print("")
        print("--------------------- Product Selection -------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        product_ID = product_codes[selection - 1]

    print("You have selected product id:", product_ID)
    return product_ID


# Gets and converts user input from string to date format
def get_date(start_end):

    flag = True

    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
            pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False

    return date


# Extracts data based on product ID within a user specified date range
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("/workspaces/codespaces-blank/Task4a_SportZone_data.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"] = pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")

    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                 (product_data["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))

    extracted_data = product_data.loc[date_range]

    return extracted_data


# Generates a total of the number of items sold for the extracted data
def calculate_total_sale(date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(
        product_id, start_date, end_date, total_sales))



def get_category():
    flag = True 
    while flag == True:
        print("-"*66)
        print("---------- SportZone Sales Analysis Module ----------- ")
        print("-"*66)
        print("")
        print("--------------------- category Selection -------------- ")
        print("Enter category code:")
        print("1.Outdoor & Camping")
        print("2.Fitness Equipment")
        print("3.Sports Clothing")
        category_choice = int(input('Enter your number selection here: '))


        if category_choice == 1:
            choice = 'Outdoor & Camping'
            flag = False

        elif category_choice == 2:
            choice = 'Fitness Equipment'
            flag = False
        
        elif category_choice == 3:
            choice = 'Sports Clothing'
            flag = False
        

    return choice


def get_data_by_category_and_date(category_type, start_date, end_date):
    all_data = pd.read_csv("/workspaces/codespaces-blank/Task4a_SportZone_data.csv")
    product_data = all_data.loc[all_data["Category"] == category_type].copy()

    product_data["Date"] = pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")

    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                (product_data["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))

    extracted_data = product_data.loc[date_range]

    return extracted_data

def calculate_category_sales(date_ID, category_type, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(
        category_type, start_date, end_date, total_sales))

def get_product_sale():
    df = pd.read_csv("/workspaces/codespaces-blank/Task4a_SportZone_data.csv")

    product_codes = df["Product ID"].unique().tolist()
   
   
    flag = True 
    while flag == True:
        print("-"*66)
        print("---------- SportZone Sales Analysis Module ----------- ")
        print("-"*66)
        print("")
        print("--------------------- category Selection -------------- ")
        print("Enter product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])
        selection_input = input('Enter your number selection here: ')
        if selection_input.isdigit():
            selection = int(selection_input)
            if 1 <= selection <= len(product_codes):
                product_ID = product_codes[selection - 1]
                flag = False
            else:
                print("Invalid selection. Please enter a number between 1 and {}.".format(len(product_codes)))
                flag = True
        else:
            print("Invalid input. Please enter a valid number.")
            flag = True

    print("You have selected product id:", product_ID)

    return product_ID

def calculate_profit_product(date_ID,product_id,start_date,end_date):
    date_ID["Profit"] = (date_ID["Sales Price"] - date_ID["Cost Price"]) * date_ID["Qty Sold"]
    total_profit = date_ID["Profit"].sum()
    print('The total profit for product {}, between {} and {} was: {}'.format(
        product_id, start_date, end_date, total_profit))




main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale(date_ID, product_id, start_date, end_date)
elif main_menu_choice == 2:
    category_type = get_category()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_category_and_date(category_type, start_date, end_date)
    calculate_category_sales(date_ID, category_type, start_date, end_date)
elif main_menu_choice == 3:
    product_id = get_product_sale()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_profit_product(date_ID,product_id,start_date,end_date)




