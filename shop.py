class ThreeFailedAttempts(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

def check_input(user_input, prices):
    if user_input not in prices:
        raise ValueError("Input not found in dictionary")

def check_affordability(user_input, prices, balance, purchase_attempts):
    if prices[user_input] > balance:
        if purchase_attempts >= 3:
            raise ThreeFailedAttempts("You have had three failed attempts.")

def check_extra_money(more_money, user_input, prices):
    more_money = float(more_money)
    if more_money <= 0:
        raise ValueError("Invalid entry, must be more than 0")

    if prices[user_input] > more_money:
        raise InsufficientFundsError("Insufficient funds even with extra money")
    return more_money

def shop():
    prices = {"Wardrobe": 75, "Rug": 20, "Art": 1000}
    balance = 100
    purchase_attempts = 0
    purchased_items = []

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
            check_input(user_input, prices)
            check_affordability(user_input, prices, balance, purchase_attempts)

            print("Sorry, you cannot afford this item")

            more_money = input("Do you have more money? If so enter the amount, if not type exit: ")
            if more_money.lower() == "exit":
                print("Goodbye")
                break

            more_money = check_extra_money(more_money, user_input, prices)

            balance -= prices[user_input]
            purchased_items.append(user_input)
            print(f"Here's your {user_input}!")

        except ValueError as e:
            print(f"Error: {e}")

        except ThreeFailedAttempts as e:
            print(f"Error: {e}")
            print("Sorry you have had the maximum three attempts")
            break

if __name__ == "__main__":
    shop()


# --- Marks (10/12) The program is executing as expected when customer has enough balance to buy the product. And your program is producing runtime errors when trying to add more money. 
