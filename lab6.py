def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")


def encoder(password):
    
    new_p = ""
    
    for digit in password:
        new_d = str((int(digit) + 3) % 10)
        new_p += new_d
    return new_p



            
        