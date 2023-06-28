class ThreeFailedAttempts(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

prices = {"Wardrobe": 75, "Rug": 20, "Art": 1000}
balance = 100
purchase_attempts = 0

print("Welcome")

while True:
    print("The items and their prices:")
    for key, value in prices.items():
        print(f"{key}: £{value}")
    print("Please type exit to leave the shop")

    user_input = input("Enter your choice: ")

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    try:
        if user_input not in prices:
            raise ValueError("Input not found in dictionary")

        if prices[user_input] > balance:
            print("Sorry, you cannot afford this item")

            if purchase_attempts >= 3:
                raise ThreeFailedAttempts("You have had three failed attempts.")

            more_money = input("Do you have more money? If so enter the amount, if not type exit: ")
            if more_money.lower() == "exit":
                print("Goodbye")
                break

            try:
                more_money = float(more_money)
                if more_money <=0:
                    raise ValueError("Invalid entry, must be more than 0")

                balance += more_money
                purchase_attempts += 1

                if prices[user_input] > more_money:
                    raise InsufficientFundsError("Insufficient funds even with extra money")

            except ValueError:
                raise ValueError("This is an invalid amount")

            else:
                balance -= prices[user_input]
                print(f"Here's your {user_input}!")

    except ValueError as e:
        print(f"Error: {e}")
    except ThreeFailedAttempts as e:
        print(f"Error {e}")
        print("Sorry you have had the maximum three attempts")
        break


