import sys

from user_input.user_input import UserInput
from postcode.validator import Validator
from postcode.formatter import Formatter

def main():
    """
    Main function acts as a command prompt menu allowing user 
    to interact with the postcode validator and formatter
    """

    print()
    print("*" * 60)
    print("\nHello! Welcome to the UK Postcode Validator/Formatter!\n")
    print("Please type the number in brackets to choose from the options below:\n")

    while True:
        print("*" * 60)
        print("\n[1] Validate a postcode")
        print("[2] Format a postcode")
        print("[3] Retreive details for a postcode")
        print("[4] Exit program\n")

        user_option = UserInput.get_user_option_entered(0)

        if user_option == 1: # Validate postcode
            postcode = UserInput.get_user_postcode_entered()
            is_valid = Validator.validate(postcode)
            if is_valid: print("Postcode '" + postcode + "' is valid!\n")
            else: print("Postcode '" + postcode + "' is invalid! Doesn't match correct format.\n")

        elif user_option == 2: # Format postcode
            postcode = UserInput.get_user_postcode_entered()
            formatted_postcode = Formatter.format(postcode)
            is_valid = Validator.validate(formatted_postcode)
            if is_valid: print("Your formatted postcode is: '" + formatted_postcode + "'\n")
            else: print("Postcode '" + postcode + "' is invalid! Doesn't match correct format.\n")
        
        elif user_option == 3:  # Retrieve postcode details
            postcode = UserInput.get_user_postcode_entered()
            print(Validator.retrieve_details(postcode))

        elif user_option == 4: # Exit
            print("Exiting the program...\n")
            sys.exit()


if __name__ == "__main__":
    main()