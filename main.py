import helpers

def main():
    while True:
        print("welcome to my program! Please choose an option: ")
        print("1. Guessing Game")
        print("2. Budget Calculator")
        print("3. Grade Calculator")
        print("4. Exit")
        print("===============================")
        choice = input("Enter your choice: ")

        print("===============================")

        if choice == "1":
            helpers.guessing_game()

        elif choice == "2":
            helpers.budget_calculator()

        elif choice == "3":
            helpers.grade_calculator()

        elif choice == "4":
            print("Thank you for using my program!")
            break
        else:
            print("Invalid choice. Please try again. ")
 
main()