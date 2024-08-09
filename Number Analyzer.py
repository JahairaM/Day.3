# This makes sure the input is a positive integer between 1 and 100
def valid_integer():
    while True:
        try:
            number = int(input("Enter a positive integer between 1 and 100: "))
            if 1 <= number <= 100:
                return number
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Enter Name
name = input("Enter your name: ")

# This keeps the program running until the user chooses to stop by saying no
while True:
# This gets a valid number from the user
    number = valid_integer()

# Specifications for the messages they get based on the number they enter
    if number % 2 != 0 and number < 60:
        print(f"{name}, {number} is Odd and less than 60.")
    elif number % 2 == 0 and 2 <= number <= 24:
        print(f"{name}, {number} is Even and less than 25.")
    elif number % 2 == 0 and 26 <= number <= 60:
        print(f"{name}, {number} is Even and between 26 and 60 inclusive.")
    elif number % 2 == 0 and number > 60:
        print(f"{name}, {number} is Even and greater than 60.")
    elif number % 2 != 0 and number > 60:
        print(f"{name}, {number} is Odd and greater than 60.")

    # This is asking if they want to continue entering numbers
    continue_program = input(f"{name}, do you want to check another number? (yes/no): ").lower()
    if continue_program != 'yes':
        print(f"Goodbye, {name}!")
        break
