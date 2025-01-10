class UserInput:
    @staticmethod
    def get_user_option_entered(user_option):
        """
        Prompts user to enter a valid number between 1 and 4
        """
        try:
            user_option = int(input("Enter a number from the options above: "))
            print()
            if user_option < 1 or user_option > 4:
                print("Invalid input. Please enter a valid integer between 1 and 4.\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 4.\n")
        return user_option
    
    @staticmethod
    def get_user_postcode_entered():
        """
        Prompts user to enter a postcode
        """
        postcode = ""
        try:
            postcode = input("Enter the postcode: ")
            print()
        except Exception as e:
            print("There was a problem when inputting your postcode: {e}")
        return postcode