from cardHolder import cardHolder

def print_menu():
    ### Print options to user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your $$. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))
        ### Check if user has enough money
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go! Thank you :)")
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if _name_ == "_main_":
    current_user = cardHolder("","","","","")

    ### Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("4627343342", 1234, "Josh", "Grifth", 150.21))
    list_of_cardHolders.append(cardHolder("2342343244", 5424, "May", "Jomma", 1350.02))
    list_of_cardHolders.append(cardHolder("6546452423", 6623, "April", "Lebbe", 321.01))
    list_of_cardHolders.append(cardHolder("4856733636", 6432, "Nova", "Lila", 199.21))
    list_of_cardHolders.append(cardHolder("4836365633", 2523, "Darm", "Noka", 152.21))

    ### Prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:  
                print("Card number not recognized. Please try again")
        except:
            print("Card number not recognized. Please try again")

    ### Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again")
        except:
            print("Invalid PIN. Please try again")

    ### Print options
    print("welcome ", current_user.get_firstname(), " :)")
    option = 0
    while (option !=4):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")
        
        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
        
    print("Thank you. Have a nice day :)")
