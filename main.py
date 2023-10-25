# Alexis Simpson
# COP3502C Lab 6
# 10/25/23

# Encodes password the user entered (numbers shifted by 3)
def encode(password):
    encoded_password = ''
    for n in password:
        encoded_password += str(int(n) + 3)

    return encoded_password


def main():
    # Prints Menu and takes in user choice
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ")
    print()
    user_choice = int(input("Please enter an option:"))

    # If the user chooses 1, it encodes the password they entered
    if user_choice == 1:
        password = input("Please enter your password to encode:")
        password = encode(password)
        print("Your password has been encoded and stored!")


if __name__ == '__main__':
    main()
