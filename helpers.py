import random

#==============================
#1. Guessing Game
#==============================


def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I generated a random number between 1 and 100. Try to guess it!")
    print("You have 5 attempts to guess the number. Good Luck!") 

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    loop = True
    
    while loop == True:
        guess = int(input("\nGuess a number between 1 and 100: "))

        if guess < number and guess >= 1: #this statement is true when the user's guess is too low.
            print("\nToo low! Try again.")  
            attempts += 1 

        elif guess > number and guess <= 100 and attempts < max_attempts: #this statement is true when the user's guess is too high.
            print("\nToo high! Try again.")
            attempts += 1


        elif guess == number : #this statement is true when the user guesses the correct number.
            print("\nCongratulations! You guessed the number!")
            print(f"\nYou guessed it in {attempts} attempts.")
            break
            

        print(f"\nAttempt {attempts} of {max_attempts}")
        
        if attempts >= max_attempts: #this statement is true when the user has used all their attempts.
            print("\nGame Over!") 
            break
    print(f"\nThe correct number was: {number}")
    print("\nThank you for playing the Guessing Game!")
    print("===============================")


# ==============================
# Budget Calculator
# ==============================


def budget_calculator():
    print("Welcome to the Budget Calculator!")

    income = float(input("Enter your monthly income (R): "))

    # Lists to store descriptive names and costs
    expense_names = []
    expense_amounts = []

    print("\n--- Enter Your Expenses ---")
    print("Enter 'done' when you are finished adding expenses.\n")

    while True:
        name = input("Enter expense name (e.g., Rent, Groceries) or 'done': ")
        if name.lower() == "done":
            break

        # Input validation for the expense amount
        try:
            amount = float(input(f"Enter amount for {name} (R): "))
            # Add data to our tracking lists
            expense_names.append(name)
            expense_amounts.append(amount)
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    # Calculate total expenses using sum() on our amounts list
    total_expenses = sum(expense_amounts)
    savings = income - total_expenses

    # Breakdown Display
    print("\n===============================")
    print("        BUDGET SUMMARY         ")
    print("===============================")
    print(f"Monthly Income:   R{income:.2f}")
    print("-------------------------------")
    print("Expenses Breakdown:")

    # Loop through lists to print items
    for i in range(len(expense_names)):
        print(f" - {expense_names[i]}: R{expense_amounts[i]:.2f}")

    print("-------------------------------")
    print(f"Total Expenses:   R{total_expenses:.2f}")
    print(f"Monthly Savings:  R{savings:.2f}")
    print("===============================\n")

    # Financial health feedback
    if savings < 0:
        print(
            "⚠️ You are spending more than you earn. Consider reducing your expenses.\n"
        )
    elif savings == 0:
        print(
            "😐 You are breaking even. Consider finding new ways to save money.\n"
        )
    else:
        print("🎉 Great job! You are saving money. Keep it up!\n")

# ==============================
# Grade Calculator
# ==============================

def grade_calculator():
    print("Welcome to the Grade Calculator!")
    

    while True:
        try:
            score = int(input("Enter your test score between 0 and 100: "))
            if score < 0 or score > 100:
                print("Invalid score. Please enter a number between 0 and 100.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

    if score <= 100 and score >=90:
        print("Test results: A")
    elif score <= 89 and score >=80:
        print("Test results: B")
    elif score <=79 and score >=70:
        print("Test results: C")
    elif score <=69 and score >=60:
        print("Test results: D")
    else:
        print("Test results: F")