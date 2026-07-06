# ============================================================
# Expense Calculator
# Student Name: Aviraj Kumar
# Module: Software Design and Development
# Description: A program that allows users create accounts,
#              track their monthly expenses by category,
#              and compare spending against their budget.
#              All data saved in a txt file so that no data
#              is lost.
# ============================================================



# This variable is to keeps track of which user is currently logged in
logged_in_user_id = None

# This is a tuple using it to store the expense categories
EXPENSE_CATEGORIES = ("Food", "Rent", "Transport", "Entertainment", "Other")

# This is the main list that stores all user accounts and each user is stored as a dictionary inside this list
myList = [
    {
        "expense_id": 1001,
        "full_name": "Aviraj Kumar",
        "email": "avirajk216@gmail.com",
        "date_of_birth": "06/02/2006",
        "monthly_budget": 400.0,
        "password": "avirajAshok",
    },
    {
        "expense_id": 1002,
        "full_name": "Danish Kumar",
        "email": "danish@gmail.com",
        "date_of_birth": "16/10/2000",
        "monthly_budget": 400.0,
        "password": "DanishAshok",
    },
    {
        "expense_id": 1003,
        "full_name": "Ashok Kumar",
        "email": "ashok216@gmail.com",
        "date_of_birth": "28/10/1983",
        "monthly_budget": 550.0,
        "password": "ashokGopal",
    }
]

# This list stores all expense records each expense is stored as a dictionary inside this list and is linked with myList using user_expense_id
user_expense_data = [
    {
        "expense_record_id": 2001,
        "user_expense_id": 1001,
        "expense_title": "Monthly Rent",
        "expense_category": "Rent",
        "expense_amount": 400.0,
        "expense_date": "01/03/2026",
        "is_paid": True
    },
    {
        "expense_record_id": 2002,
        "user_expense_id": 1001,
        "expense_title": "Grocery Shopping",
        "expense_category": "Food",
        "expense_amount": 85.50,
        "expense_date": "05/03/2026",
        "is_paid": True
    },
    {
        "expense_record_id": 2003,
        "user_expense_id": 1002,
        "expense_title": "Bus Pass",
        "expense_category": "Transport",
        "expense_amount": 55.00,
        "expense_date": "01/03/2026",
        "is_paid": False
    }
]


# This is the name of the file where all the users data is saved.
FILE_NAME = "avirajKumar_data.txt"


# Try except is a way of error handling, try means this try type of error is expected like a user entered a letter instead of a number and then except tells what should happen in that case.
def save_data():
    try:
        # The "w" open the txt file to put data in it if the file do not exit it creates a new file and puts data in it.
        with open(FILE_NAME, "w") as file:
            # Write each user record on a separate line
            file.write("[\n")
            for i, user in enumerate(myList):
                if i < len(myList) - 1:
                    file.write(str(user) + ",\n")
                else:
                    file.write(str(user) + "\n")
            file.write("]\n")
            # SPLIT is a simple text between the two lists that separate the both lists so that we know which one is user's credential  list and which one is the users expense list
            file.write("---SPLIT---\n")
            # Write each expense record on a separate line
            file.write("[\n")
            for i, expense in enumerate(user_expense_data):
                if i < len(user_expense_data) - 1:
                    file.write(str(expense) + ",\n")
                else:
                    file.write(str(expense) + "\n")
            file.write("]\n")
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")


def load_data():
    global myList, user_expense_data
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            # If file is empty, just use the default sample data already in the lists
            if content.strip() == "":
                print("No saved data found. Starting with default data.")
                return
            # Split the file content into two parts using the marker
            parts = content.split("\n---SPLIT---\n")
            # eval() converts the text back into a Python list
            myList.clear()
            myList.extend(eval(parts[0]))
            user_expense_data.clear()
            user_expense_data.extend(eval(parts[1]))
        print("Data loaded successfully.")
    except FileNotFoundError:
        # This runs if the txt file does not exist yet
        print("No saved data found. Starting with default data.")
    except Exception as e:
        print(f"Error loading data: {e}")




#Exit Function
def exit_program():
    print("Thank you for using Expense Calculator! Goodbye!")

# Function to add rent
def addRent():
    print("Add Rent")
    try:
        rentPY = int(input("Please enter your Rent amount: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        addRent()
        return

    # Asking if rent is paid and store True or False (Boolean)
    is_rent_paid_input = input("Is your rent paid? Yes/No: ")
    if is_rent_paid_input == "yes":
        is_rent_paid = True
    else:
        is_rent_paid = False

    expense_date_input = input("Please enter the date of this expense (DD/MM/YYYY): ")

    # Auto generate a new unique ID for this expense record
    # We add 2001 to the length of the list so IDs start at 2001 and go up to the length of the list
    expense_record_id = 2001 + len(user_expense_data)

    # Add the new rent expense to user_expense_data list and logged_in_user_id links this expense to the current user
    user_expense_data.append({
        "expense_record_id": expense_record_id,
        "user_expense_id": logged_in_user_id,
        "expense_title": "Rent",
        "expense_category": "Rent",
        "expense_amount": rentPY,
        "expense_date": expense_date_input,
        "is_paid": is_rent_paid
    })
    save_data()
    print(f"Rent of £{rentPY} added successfully.")

    continue_choice = input("Do you want to add more expenses? Yes/No: ")
    if continue_choice == "No":
        user_choice2()
    else:
        add_Expense()


def travel_expense():
    # This function asks user for travel expense amount and if they have paid that and then saves it to user_expense_data
    print("Add Travel Expense")
    try:
        travel_expensePY = int(input("Please enter your Travel expense amount: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        travel_expense()
        return

    is_travel_paid_input = input("Is this travel expense paid? Yes/No: ")
    if is_travel_paid_input == "Yes":
        is_travel_paid = True
    else:
        is_travel_paid = False

    expense_date_input = input("Please enter the date of this expense (DD/MM/YYYY): ")

    expense_record_id = 2001 + len(user_expense_data)

    user_expense_data.append({
        "expense_record_id": expense_record_id,
        "user_expense_id": logged_in_user_id,
        "expense_title": "Travel",
        "expense_category": "Transport",
        "expense_amount": travel_expensePY,
        "expense_date": expense_date_input,
        "is_paid": is_travel_paid
    })
    save_data()
    print(f"Travel expense of £{travel_expensePY} added successfully.")
    user_choice2()


def other_expense():
    # This function lets user to name their own expense and enter the amount they have spent on it and then saves it to user_expense_data

    print("Add Other Expense")
    other_expense_name = input("Please enter your expense name: ")
    try:
        other_expensePY = int(input(f"Please enter the amount you have spent on {other_expense_name}: £"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        other_expense()
        return


    is_other_paid_input = input("Is this expense paid? Yes/No: ")
    if is_other_paid_input == "yes":
        is_other_paid = True
    else:
        is_other_paid = False

    expense_date_input = input("Please enter the date of this expense (DD/MM/YYYY): ")

    expense_record_id = 2001 + len(user_expense_data)

    user_expense_data.append({
        "expense_record_id": expense_record_id,
        "user_expense_id": logged_in_user_id,
        "expense_title": other_expense_name,
        "expense_category": "Other",
        "expense_amount": other_expensePY,
        "expense_date": expense_date_input,
        "is_paid": is_other_paid
    })
    save_data()
    print(f"Expense of £{other_expensePY} added successfully.")
    add_Expense()

#  Add grocery (usual expenses) expenses
def usual_expenses():
    print("Add Grocery Expenses")

    try:
        parathaPY = float(input("Number of frozen parathas packets purchased this month (£3.50 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        nuggetsPY = float(input("Number of frozen Nuggets packets purchased this month (£3.30 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        friesPY = float(input("Number of frozen Fries packets purchased this month (£1.65 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        chickenPY = float(input("Number of KGs of chicken purchased this month (£5.00 per KG): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        eggsPY = float(input("Number of packets of eggs purchased this month (£1.40 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        milkPY = float(input("Number of packets of Milk purchased this month (£2.40 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        breadPY = float(input("Number of packets of Bread purchased this month (£0.74 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        tomatoPY = float(input("Number of packets of Tomato purchased this month (£0.50 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        biscuitPY = float(input("Number of packets of Biscuit purchased this month (£1.00 per packet): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return

    try:
        onionPY = float(input("Number of KGs of Onion purchased this month (£1.00 per KG): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        usual_expenses()
        return


    # Multiply quantity by price to get total cost for each item
    parathaPY = parathaPY * 3.50
    nuggetsPY = nuggetsPY * 3.30
    friesPY = friesPY * 1.65
    chickenPY = chickenPY * 5.00
    eggsPY = eggsPY * 1.40
    milkPY = milkPY * 2.40
    breadPY = breadPY * 0.74
    tomatoPY = tomatoPY * 0.50
    biscuitPY = biscuitPY * 1.00
    onionPY = onionPY * 1.00

    # Add all items cost together to get the total grocery bill
    total_usualExpense = parathaPY + nuggetsPY + friesPY + chickenPY + eggsPY + milkPY + breadPY + tomatoPY + biscuitPY + onionPY
    print(f"\nTotal grocery expense this month: £{round(total_usualExpense, 2)}")

    is_grocery_paid_input = input("Is this grocery expense paid? Yes/No: ")
    if is_grocery_paid_input == "Yes":
        is_grocery_paid = True
    else:
        is_grocery_paid = False

    expense_date_input = input("Please enter the date of this expense (DD/MM/YYYY): ")

    expense_record_id = 2001 + len(user_expense_data)

    # Store the total grocery amount as one single expense record
    user_expense_data.append({
        "expense_record_id": expense_record_id,
        "user_expense_id": logged_in_user_id,
        "expense_title": "Grocery Shopping",
        "expense_category": "Food",
        "expense_amount": round(total_usualExpense, 2),
        "expense_date": expense_date_input,
        "is_paid": is_grocery_paid,
        "Paratha": parathaPY,
        "Nuggets": nuggetsPY,
        "Fries": friesPY,
        "Chicken": chickenPY,
        "Eggs": eggsPY,
        "Milk": milkPY,
        "Bread": breadPY,
        "Tomato": tomatoPY,
        "Biscuit": biscuitPY,
        "Onion": onionPY,
    })


    save_data()
    print("Grocery expenses added successfully.")
    user_choice2()


def add_Expense():
    # This is a function inside a function
    # user_choice3 is the menu for adding expenses
    # It is defined inside add_Expense so it only exists here
    def user_choice3():
        list_1 = [1, "Add rent"]
        list_2 = [2, "Add Grocery Expenses"]
        list_3 = [3, "Travel"]
        list_4 = [4, "Others"]
        list_5 = [5, "Go back"]

        print("\nWhat type of expense would you like to add?")
        print("1. Add rent")
        print("2. Add Grocery Expenses")
        print("3. Travel")
        print("4. Others")
        print("5. Go back")
        try:
            user_choice3_list = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            user_choice3()
            return
        if user_choice3_list == list_1[0]:
            addRent()
        elif user_choice3_list == list_2[0]:
            usual_expenses()
        elif user_choice3_list == list_3[0]:
            travel_expense()
        elif user_choice3_list == list_4[0]:
            other_expense()
        elif user_choice3_list == list_5[0]:
            user_choice2()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            user_choice3()

    user_choice3()


# Delete user function

def deleteUser():
    print("Delete Account")
    deleteUser_choice = input("Are you sure you want to delete your account? Yes/No: ")

    if deleteUser_choice == "No":
        print("You selected not to delete your account. Let's continue.")
        user_choice2()
    else:

        try:
            expenseIDPY = int(input("Please enter your Expense ID to confirm: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            deleteUser()
            return

        emailPY = input("Please enter your email to confirm: ")
        passwordPY = input("Please enter your password to confirm: ")

        for user in myList:
            if user["expense_id"] == expenseIDPY and user["email"] == emailPY and user["password"] == passwordPY:
                myList.remove(user)

                # Remove all expenses that belong to this user from user_expense_data
                expenses_to_keep = [expense for expense in user_expense_data if expense["user_expense_id"] != expenseIDPY]

                # Clear the original list and refill it with only the kept expenses
                user_expense_data.clear()
                user_expense_data.extend(expenses_to_keep)
                save_data()

                print(f"Your account and all your expenses have been deleted successfully!")
                user_choice()
                return

        print("Your credentials do not match. Please try again.")
        user_choice2()


# Check user data function

def checkUser_data():
    print("Your Expenses")
    recordFound = False

    # Loop through every expense and only show ones that belong to the logged in user
    for expense in user_expense_data:
        if expense["user_expense_id"] == logged_in_user_id:
            recordFound = True
            # Change True/False to readable text for display
            paid_status = "Paid" if expense["is_paid"] else "Unpaid"
            print(f"  ID: {expense['expense_record_id']} | {expense['expense_title']} | £{expense['expense_amount']} | {expense['expense_category']} | {expense['expense_date']} | {paid_status}")

    if not recordFound:
        print("No expenses found for your account.")

    user_choice2()


# Update user record function
def updateRecord():
    print("Update Expense Record")

    # First showing the user their expenses so they know which ID to enter
    recordFound = False
    for expense in user_expense_data:
        if expense["user_expense_id"] == logged_in_user_id:
            recordFound = True
            paid_status = "Paid" if expense["is_paid"] else "Unpaid"
            print(f"  ID: {expense['expense_record_id']} | {expense['expense_title']} | £{expense['expense_amount']} | {expense['expense_category']} | {paid_status}")

    if not recordFound:
        print("No expenses found for your account.")
        user_choice2()
        return


    try:
        update_id = int(input("Please enter your ID to update: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        updateRecord()
        return

    # Looking for the expense with the matching ID that matches to the logged in user
    for expense in user_expense_data:
        if expense["expense_record_id"] == update_id and expense["user_expense_id"] == logged_in_user_id:
            print(f"\nUpdating: {expense['expense_title']}")
            print("1. Expense title")
            print("2. Expense amount")
            print("3. Expense category")
            print("4. Mark as paid or unpaid")

            try:
                update_choice = int(input("Please enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                updateRecord()
                return

            if update_choice == 1:
                expense["expense_title"] = input("Enter new title: ")
                print("Title updated successfully.")
                save_data()

            elif update_choice == 2:
                expense["expense_amount"] = float(input("Enter new amount: £"))
                print("Amount updated successfully.")
                save_data()

            elif update_choice == 3:
                print(f"Categories available: {EXPENSE_CATEGORIES}")
                expense["expense_category"] = input("Enter new category: ")
                print("Category updated successfully.")
                save_data()

            elif update_choice == 4:
                # "not" flips the Boolean - if it was True it becomes False and the other way round
                expense["is_paid"] = not expense["is_paid"]
                status = "Paid" if expense["is_paid"] else "Unpaid"
                print(f"Payment status updated to: {status}")
                save_data()

            else:
                print("Invalid choice.")

            user_choice2()
            return

    print(f"No expense found with ID {update_id} in your account.")
    user_choice2()


# Search Function
def search_expenses():
    # This function allows user check user's for their account's details by using email or check if their rent is paid

    print("Search")
    print("1. Check your Account details")
    print("2. Check if your rent is paid")

    try:
        search_choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        search_expenses()
        return

    if search_choice == 1:
        # Search for a user by their email address in myList
        search_email = input("Enter the email address to search for: ")
        userFound = False

        for user in myList:
            if user["email"] == search_email:
                userFound = True
                print(f"\nAccount found!")
                print(f"  Name: {user['full_name']}")
                print(f"  Email: {user['email']}")
                print(f"  Expense ID: {user['expense_id']}")

        if not userFound:
            print("No account found with that email address.")

    elif search_choice == 2:
        # Check if the logged in user has paid their rent in user_expense_data for rent expenses
        rentFound = False

        for expense in user_expense_data:
            if expense["user_expense_id"] == logged_in_user_id and expense["expense_category"] == "Rent":
                rentFound = True
                paid_status = "Paid" if expense["is_paid"] else "Unpaid"
                print(f"\n  Rent: {expense['expense_title']} | £{expense['expense_amount']} | {expense['expense_date']} | {paid_status}")

        if not rentFound:
            print("No rent expenses found for your account.")

    else:
        print("Invalid choice.")

    user_choice2()


# Display all function to check the user's monthly summery
def display_all():
    print("Your Monthly Expense Summary")

    # Find the logged in user's monthly budget from myList
    monthly_budget = 0
    for user in myList:
        if user["expense_id"] == logged_in_user_id:
            monthly_budget = user["monthly_budget"]

    # These variables will add up spending in each category
    total_spent = 0.0
    total_rent = 0.0
    total_food = 0.0
    total_transport = 0.0
    total_entertainment = 0.0
    total_other = 0.0

    print("All your expenses:")

    recordFound = False
    for expense in user_expense_data:
        if expense["user_expense_id"] == logged_in_user_id:
            recordFound = True
            paid_status = "Paid" if expense["is_paid"] else "Unpaid"
            # :< 25 it means to left align leave a space of 25 characters, we do it so that the output looks neet and clean.
            print(f"  {expense['expense_title']:<25} £{expense['expense_amount']:<10} {expense['expense_category']:<15} {expense['expense_date']:<12} {paid_status}")

            # Add each expense to the running total
            total_spent = total_spent + expense["expense_amount"]

            # Add to the correct category total
            if expense["expense_category"] == "Rent":
                total_rent = total_rent + expense["expense_amount"]
            elif expense["expense_category"] == "Food":
                total_food = total_food + expense["expense_amount"]
            elif expense["expense_category"] == "Transport":
                total_transport = total_transport + expense["expense_amount"]
            elif expense["expense_category"] == "Entertainment":
                total_entertainment = total_entertainment + expense["expense_amount"]
            elif expense["expense_category"] == "Other":
                total_other = total_other + expense["expense_amount"]

    if not recordFound:
        print("No expenses found for your account.")
        user_choice2()
        return

    # Calculate how much money is left from the budget
    remaining_budget = monthly_budget - total_spent

    # the round(value, 2) means it will round up the float number to 2 digit after the decimal.
    print("-" * 70)
    print(f"  Monthly Budget:          £{round(monthly_budget, 2)}")
    print(f"  Total Spent:             £{round(total_spent, 2)}")
    print(f"  Remaining Budget:        £{round(remaining_budget, 2)}")
    print(f"  Breakdown by Category:")
    print(f"  Rent:                  £{round(total_rent, 2)}")
    print(f"  Food / Grocery:        £{round(total_food, 2)}")
    print(f"  Transport:             £{round(total_transport, 2)}")
    print(f"  Entertainment:         £{round(total_entertainment, 2)}")
    print(f"  Other:                £{round(total_other, 2)}")

    # Tell user if he has gone over budget
    if total_spent > monthly_budget:
        print(f"\n  WARNING: You have gone over your budget by £{round(total_spent - monthly_budget, 2)}!")
    else:
        print(f"\n  You are within your budget. Well done!")

    grocery_listQuestion = input("\nDo you want to see your complete Grocery list? Yes/No: ")
    if grocery_listQuestion == "yes":
        print("\n--- Grocery Breakdown ---")
        groceryFound = False
        # Loop through expenses and find grocery records that have individual item data
        for expense in user_expense_data:
            if expense["user_expense_id"] == logged_in_user_id and expense["expense_title"] == "Grocery Shopping":
                groceryFound = True
                print(f"\n  Grocery record ID: {expense['expense_record_id']} | Date: {expense['expense_date']}")
                print(f"  {'Item':<15} {'Amount'}")
                print(f"  {'-' * 30}")
                # Check each item — only show it if it exists in this expense record
                # Not all grocery records will have individual items if added before this feature
                if "Paratha" in expense:
                    print(f"  {'Paratha':<15} £{round(expense['Paratha'], 2)}")
                if "Nuggets" in expense:
                    print(f"  {'Nuggets':<15} £{round(expense['Nuggets'], 2)}")
                if "Fries" in expense:
                    print(f"  {'Fries':<15} £{round(expense['Fries'], 2)}")
                if "Chicken" in expense:
                    print(f"  {'Chicken':<15} £{round(expense['Chicken'], 2)}")
                if "Eggs" in expense:
                    print(f"  {'Eggs':<15} £{round(expense['Eggs'], 2)}")
                if "Milk" in expense:
                    print(f"  {'Milk':<15} £{round(expense['Milk'], 2)}")
                if "Bread" in expense:
                    print(f"  {'Bread':<15} £{round(expense['Bread'], 2)}")
                if "Tomato" in expense:
                    print(f"  {'Tomato':<15} £{round(expense['Tomato'], 2)}")
                if "Biscuit" in expense:
                    print(f"  {'Biscuit':<15} £{round(expense['Biscuit'], 2)}")
                if "Onion" in expense:
                    print(f"  {'Onion':<15} £{round(expense['Onion'], 2)}")
                print(f"  {'-' * 30}")
                print(f"  {'Total':<15} £{round(expense['expense_amount'], 2)}")

        if not groceryFound:
            print("No grocery records found for your account.")
    else:
        user_choice2()
    user_choice2()


# Signup function

def signup():
    print("Sign Up")
    print("Please enter your details to register.")

    fullNamePy = input("Please enter your full name: ")

    useremailPY = input("Please enter your email: ")

    # Check if this email is already registered
    # Loop through all users and set emailExists to True if found
    emailExists = False
    for user_email in myList:
        if user_email["email"] == useremailPY:
            emailExists = True

    if emailExists:
        print("An account with this email already exists! Please login to continue.")
        user_choice()
        return

    # Ask for date of birth and split it into day, month, year
    DOBPY = input("Enter your date of birth (DD/MM/YYYY): ")
    DOBPY_parts = DOBPY.split("/")

    try:
        DOBPY_day = int(DOBPY_parts[0])
    except ValueError:
        print("Invalid input. Please enter a number.")
        signup()
        return

    try:
        DOBPY_month = int(DOBPY_parts[1])
    except ValueError:
        print("Invalid input. Please enter a number.")
        signup()
        return

    try:
        DOBPY_year = int(DOBPY_parts[2])
    except ValueError:
        print("Invalid input. Please enter a number.")
        signup()
        return


    # Calculate age by subtracting birth year from current year
    age = 2026 - DOBPY_year

    # If the user's birthday has not happened yet this year, subtract 1 from age
    if DOBPY_month > 3:
        age = age - 1
    elif DOBPY_month == 3:
        if DOBPY_day > 26:
            age = age - 1

    isAdult = False
    if age >= 18:
        isAdult = True
        print(f"Your age is {age} and an Adult.")
    else:
        isAdult = False
        print(f"your age is {age}, and not an Adult, so use carefully!")
        return

    try:
        monthlyBudget_PY = float(input("Please enter your monthly budget: £"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        signup()
        return

    passwordPY = input("Enter your password (minimum 8 characters): ")

    # Keep asking for password until it is at least 8 characters long
    while len(passwordPY) < 8:
        print("Password is too short. Please enter at least 8 characters.")
        passwordPY = input("Enter your password: ")

    confirmPasswordPY = input("Confirm your password: ")

    # Keep asking until both passwords match
    while confirmPasswordPY != passwordPY:
        print("Passwords do not match. Please try again.")
        exitOption = input("Do you want to exit? Yes/No: ")
        if exitOption == "Yes":
            print("Thank you for using Expense Calculator!")
            return
        else:
            passwordPY = input("Enter your password: ")
            confirmPasswordPY = input("Confirm your password: ")
    else:
        # Auto generate a new unique expense ID based on list length
        expenseIDPY = 1001 + len(myList)
        print(f"\nAccount created successfully!")
        print(f"Your Expense ID is: {expenseIDPY}. Please remember this as you need it to login.")

        myList.append({
            "expense_id": expenseIDPY,
            "full_name": fullNamePy,
            "email": useremailPY,
            "date_of_birth": DOBPY,
            "monthly_budget": monthlyBudget_PY,
            "password": passwordPY,
        })
        save_data()
        user_choice()


# Login function
def login():
    # Making logged_in_user_id global so that it can also be used outside of this function
    global logged_in_user_id
    print("Login")

    try:
        expenseIDPY = int(input("Please enter your Expense ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        login()
        return


    emailPY = input("Enter your email: ")
    passwordPY = input("Enter your password: ")

    # Check all three credentials match for the same user
    for user in myList:
        if user["expense_id"] == expenseIDPY and user["email"] == emailPY and user["password"] == passwordPY:
            logged_in_user_id = user["expense_id"]
            print(f"\nLogin successful! Welcome {user['full_name']} to Expense Calculator!")
            user_choice2()
            return

    print("Your credentials do not match. Please try again.")
    user_choice()



# After login options
def user_choice2():
    # This is the menu shown after login - user can add, check, update, delete, search or display expenses

    list_1 = [1, "Add expense"]
    list_2 = [2, "Check your expenses"]
    list_3 = [3, "Update an expense"]
    list_4 = [4, "Delete your account"]
    list_5 = [5, "Search"]
    list_6 = [6, "Display summary"]
    list_7 = [7, "Exit"]

    print("\nWhat would you like to do?")
    print("1. Add expense")
    print("2. Check your expenses")
    print("3. Update an expense")
    print("4. Delete your account")
    print("5. Search")
    print("6. Display monthly summary")
    print("7. Exit")

    try:
        user_choice2_list = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        user_choice2()
        return

    if user_choice2_list == list_1[0]:
        add_Expense()
    elif user_choice2_list == list_2[0]:
        checkUser_data()
    elif user_choice2_list == list_3[0]:
        updateRecord()
    elif user_choice2_list == list_4[0]:
        deleteUser()
    elif user_choice2_list == list_5[0]:
        search_expenses()
    elif user_choice2_list == list_6[0]:
        display_all()
    elif user_choice2_list == list_7[0]:
        exit_program()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
        user_choice2()


# Main options to ask your on very first
def user_choice():
    # This is the main menu shown at the start of the program - user can login, signup or exit

    list_1 = [1, "Login"]
    list_2 = [2, "Signup"]
    list_3 = [3, "Exit"]

    print("Welcome! What would you like to do?")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    try:
        user_choice1 = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        user_choice()
        return

    if user_choice1 == list_1[0]:
        login()
    elif user_choice1 == list_2[0]:
        signup()
    elif user_choice1 == list_3[0]:
        exit_program()
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
        user_choice()


# PROGRAM STARTS FROM HERE

print("Welcome to Expense Calculator!")
print("Track your spending and manage your budget.")


load_data()
user_choice()   
