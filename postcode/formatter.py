class Formatter:

    @staticmethod
    def get_postcode_formats():
        """
        Returns the acceptable formats for a UK Postcode as a tuple
        """
        return ("AA9 9AA", "AA99 9AA", "A9 9AA", "A99 9AA", "A9A 9AA", "AA9A 9AA")
    
    @staticmethod
    def format(postcode):
        """
        Returns a formatted postcode which:
            - Has any leading or trailing whitespace removed
            - Has a space added between outward and inward codes if missing
            - Has all letters uppercase
        """
        formatted_postcode = postcode.strip()
        formatted_postcode = Formatter.get_postcode_with_space(formatted_postcode)
        formatted_postcode = formatted_postcode.upper()
        return formatted_postcode
    
    @staticmethod
    def convert_postcode(postcode):
        """
        Converts a user's inputted postcode letters to 'A' and
        digits to '9'

        Used to eventually see if user postcode matches accepted formats
        """
        converted_postcode = ""
        for char in postcode:
            if char.isalpha(): char = 'A'
            elif char.isdigit(): char = '9'
            converted_postcode += char
        return converted_postcode
    
    @staticmethod
    def get_postcode_with_space(postcode):
        """
        For formatting, returns a postcode with a space if not entered by user
        """
        postcode_with_space = ""
        if " " not in postcode:
            postcode_with_space = postcode[:-3] + " " + postcode[-3:]
            return postcode_with_space
        return postcode # Already has space
    
    @staticmethod
    def get_postcode_area(outward_code):
        """
        Returns the postcode area based on the outward code

        The area can be 1 or 2 characters long and is alphabetical
        """
        outward_code_length = len(outward_code)

        if outward_code_length == 2: return outward_code[0]
        elif outward_code_length == 3:
            second_char = outward_code[1] # Check the second char
            if second_char.isalpha(): # If letter, then it is part of the area
                return outward_code[0:2]
            elif second_char.isdigit(): # If digit, it is part of the district
                return outward_code[0]
        elif outward_code_length == 4: return outward_code[0:2]
        else: return ""
    
    @staticmethod
    def get_postcode_district(outward_code):
        """
        Returns the postcode district based on the outward code

        The district can be either 1 or 2 digits, or a digit followed by a letter
        """
        outward_code_length = len(outward_code)

        if outward_code_length == 2: return outward_code[1]
        elif outward_code_length == 3:
            second_char = outward_code[1] # Check the second char
            if second_char.isalpha(): # If letter, then it is part of the area
                return outward_code[2:]
            elif second_char.isdigit(): # If digit, it is part of the district
                return outward_code[1:]
        elif outward_code_length == 4: return outward_code[2:]
        else: return ""
    
    @staticmethod
    def get_postcode_sector(inward_code):
        """
        Returns the postcode sector based on the inward code

        The sector is a single digit, and the first character of the inward code
        """
        return inward_code[0]
    
    @staticmethod
    def get_postcode_unit(inward_code):
        """
        Returns the postcode unit based on the inward code

        A unit is always the final two characters of the inward code
        """
        return inward_code[1:]