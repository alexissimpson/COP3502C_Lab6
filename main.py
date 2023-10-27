# Alexis Simpson
# COP3502C Lab 6
# 10/25/23

# Encodes password the user entered (numbers shifted by 3)
def encode(password):
    encoded_password = ''
    for n in password:
        encoded_password += str((int(n) + 3) % 10)
    return encoded_password

# Decodes the encoded password and returns the original password
def decoder(e_password):
    password = ""
    for digit in e_password:
        new_d = str((int(digit) - 3) % 10)
        password += new_d
    return password


def main():
    # Prints Menu
    def menu():
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ")
        print()
        
    password = ""


    # Prints the menu and prompts user for choice
    menu()
    user_choice = int(input("Please enter an option: "))

    # Loops until user enters option 3
    while True:
        # If the user chooses 1, it encodes the password they entered
        if user_choice == 1:
            password = input("Please enter your password to encode: ")
            password_e = encode(password)
            print("Your password has been encoded and stored!\n")
        # If the user chooses 2, it ouputs the encoded password and the original password
        elif user_choice == 2:
            if password_e:
                print(f"The encoded password is {password_e}, and the original password is {decoder(password_e)}.")
            else:
                print("Please enter a password to encode first.")
        elif user_choice == 3:
            break
        else:
            print("Invalid option. Please enter either 1, 2, or 3.")

        # Prints the menu and prompts user for choice
        menu()
        user_choice = int(input("Please enter an option: "))

if __name__ == '__main__':
    main()
