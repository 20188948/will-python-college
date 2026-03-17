import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. time taken to resolve different issues ")
        print("### 3. issues and resolutions based on region")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
        else:    
            print('Choice accepted!')
            flag = False

    return choice


# Submenu for totals
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = [
        "Customer Account Issue",
        "Delivery Issue",
        "Collection Issue",
        "Service Complaint"
    ]

    issueType = issueTypeList[choice-1]
    return issueType


def time_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Time taken to resolve issues ########")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = [
        "Customer Account Issue",
        "Delivery Issue",
        "Collection Issue",
        "Service Complaint"
    ]

    issueType = issueTypeList[choice-1]
    return issueType
    


# Region menu
def region_menu():
    flag = True

    while flag:

        print("####################################################")
        print("#### issues and resolutions based on region ########")
        print("####################################################")
        print("")
        print("########## Please select a region ##########")
        print("### 1.Scotland")   
        print("### 2.North West") 
        print("### 3.North East")
        print("### 4.North Wales")
        print("### 5.South Wales")
        print("### 6.West Midlands")
        print("### 7.East Midlands")
        print("### 8.East of England")
        print("### 9.South West")
        print("### 10.South East") 
        print("### 11.London")
        print("### 12.Yorkshire and The Humber")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    region_list = [
        "Scotland",
        "North West",
        "North East",
        "North Wales",
        "South Wales",
        "West Midlands",
        "East Midlands",
        "East of England",
        "South West",
        "South East",
        "London",
        "Yorkshire and The Humber"
    ]

    region = region_list[choice-1]
    return region


# Get totals by issue type
def get_total_data(total_menu_choice):

    issues = pd.read_csv("Task4a_data.csv")

    total = issues['Issue Type'].value_counts().get(total_menu_choice, 0)

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg


# Time data 
def get_time_data(total_menu_choice):

    df = pd.read_csv("Task4a_data.csv")

    filtered_df = df[df["Issue Type"] == total_menu_choice]

    avg_time = filtered_df["Days To Resolve"].mean()

    msg = "The average time to resolve {} issues was: {:.2f} days".format(total_menu_choice, avg_time)
    return msg


# Region data
def get_region_data(region_name):

    df = pd.read_csv("Task4a_data.csv")

    filtered = df[df["Region"] == region_name]

    total = filtered["Issue Type"].count()

    msg = "The total number of issues in {} was: {}".format(region_name, total)
    return msg


# MAIN PROGRAM
main_menu_choice = main_menu()

if main_menu_choice == "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))

elif main_menu_choice == "2":
    total_menu_choice = time_menu()
    print(get_time_data(total_menu_choice))

elif main_menu_choice == "3":
    region_choice = region_menu()
    print(get_region_data(region_choice))