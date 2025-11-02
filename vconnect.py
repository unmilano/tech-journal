# this top section is the exact same function as vconnect starter.txt, but completely automated
import getpass

passw = getpass.getpass() # this asks for the user's password
from pyVim.connect import SmartConnect
import ssl
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host="10.0.17.3", user="anthony-adm@anthony.local", pwd=passw, sslContext=s)
aboutInfo=si.content.about
print(aboutInfo)
print(aboutInfo.fullName)

# this is the beginning of the menu code

def show_menu():
    """
    Displays a simple menu and handles user input.
    """
    # This loop will continue forever until the user chooses to exit
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Exit")
        print("-----------------")

        # Get input from the user
        choice = input("Enter your choice (1-5): ")

        # Handle the user's choice
        if choice == '1':
            print("\nYou selected Option 1.")
            # Add code for Option 1 here
        
        elif choice == '2':
            print("\nYou selected Option 2.")
            # Add code for Option 2 here
        
        elif choice == '3':
            print("\nYou selected Option 3.")
            # Add code for Option 3 here
        
        elif choice == '4':
            print("\nYou selected Option 4.")
            # Add code for Option 4 here
        
        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            break  # This breaks out of the while loop
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# This is the standard way to run the main function in a Python script
if __name__ == "__main__":
    show_menu()
