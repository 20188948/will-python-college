#Accepts input of loyalty card number and validates it
def loyalty_card_check (): 
    valid = True

    while valid == False:

        card_number = input("Please enter the loyalty card number: ")

        if card_number.isdigit():
            if len(card_number) >= 8:
                valid = True
                return card_number
            else:
                print("You did not enter a valid loyalty card number.")
                print("Loyalty card number must be 8 characters long.")
                
        else:
            print("You did not enter a valid loyalty card number.")
            print("Loyalty card number must contain only digits.")
            valid = False

#Allows user to select the platform used for the purchase
def get_platform():
    valid = False

    while valid == False:
        print("Please select the purchase platform for this transaction")
        print("1. Online")
        print("2. In-store")
        selection = input("Enter choice here (1 or 2): ")

        if selection == 1:
            platform = "Online"
            valid = True
        elif selection == 2:
            platform = "In-Store"
            valid = True
        else:
            print("Sorry you have not entered a valid option.")
            valid = False

    return platform


#Allows the user to enter the value and category of each item purchased
def get_items (prices, categories):
    end_transaction = False

    item_count = 0

    while end_transaction == False:
        item_count += 1
        
        valid_price = False
        valid == False

        while valid_price == False:

            print("Please enter the value of item {}.".format(item_count))
            print("Enter X when finished")
            temp_price = input("Item {} : £".format(item_count))
        
            if temp_price.lower() == "x":
                end_transaction = True
                valid = True
                break
            else:
                try:
                    float(temp_price)
                except:
                    print("Sorry, you did not enter a valid price")
                    end_transaction == False
                else:    
                    temp_price = float(temp_price)
                    prices.append(temp_price)
                    valid_price = True

        
     
        while valid == False:
            print("Please enter the category choice for item {}.")
            print("1. Home Electrical.")
            print("2. Computing and Gaming")
            print("3. Accessories and Consumables")
            choice = input("Category: ")

            if choice == "1":
                temp_cat = "Home Electrical"
                categories.append(temp_cat)
                valid == True
            elif choice == "2":
                temp_cat = "Computing and Gaming"
                categories.append(temp_cat)
                valid == True 
            elif choice == "3":
                temp_cat = "Accessories and Consumables"
                categories.append(temp_cat)
                valid == True 
            else:
                print("Sorry you have not entered a valid option.")
                valid = False

#Calculates the number of points earned for each product purchased
def calculate_points (prices, categories, points_earned):
    
    for i in range(len(prices)):
        value = int(prices[i])
        category = categories[i]
        if category ==  "Computing and Gaming":
            if value > 500:
                initial_pts = 2000
                extra_pts = (value - 500) * 2
                pts = initial_pts + extra_pts
                
            else:
                pts = value * 4
                
        elif category == "Home Electrical": 
            pts = value * 4
           
        else:
            pts = value * 3


        points_earned.append(pts)     
        


def main ():
    prices = []
    categories = []
    points_earned = []
    card_number = loyalty_card_check()
    platform = get_platform()
    
    get_items(prices, categories)
    calculate_points (prices, categories)

    total_value = sum(prices)
    points_subtotal = sum(points_earned)
    if platform == "In-Store":
        bonus_pts = total_value* 2
    else:
        bonus_pts = 0

    final_pts = points_subtotal + bonus_pts

   
    print("-"*60)
    print("Transaction summary for customer {}".format(card_number))
    print("-"*60)
    print("Final total value of this transaction was £ {:.2f}".format(total_value))
    print('Here is a summary of the points you have earned:')
    for i in range(points_earned):
        print("Item {}. {} pts ".format(i+1, points_earned[i]))
    print("-"*60)
    print("Points subtotal {}: ".format(points_subtotal))
    print("-"*60)
    print("Bonus points earned {}: ".format(bonus_pts))
    print("-"*60)
    print("-"*60)
    print("Final points total: {}".format(final_pts))
    print("-"*60)
    print("-"*60)


main()