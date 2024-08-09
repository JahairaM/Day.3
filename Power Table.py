#First Message
print("Learn your squares and cubes!")


# Repeat until the user says stop
while True:
    # Ask the user to enter an integer
    num = int(input("\nEnter an integer: "))

    # Table headers
    print("\nNumber  Squared  Cubed")
    print("======  =======  ======")

    # Loop through numbers from 1 to the user's number
    for i in range(1, num + 1):
        # Print the number, its square, and its cube
        #The <6 means to the left and 5 spaces open after (self reminder)
        print(f"{i:<6}  {i ** 2:<7}  {i ** 3}")

    # Asking the user if they want to continue
    cont = input("\nWould you like to contuine? (y/n): ").strip().lower()

    # Stop if the user enters anything other than 'y'
    if cont != 'y':
        break