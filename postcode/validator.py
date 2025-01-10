from .formatter import Formatter

class Validator:
    @staticmethod
    def validate(postcode):
        """
        Returns whether or not the user inputted postcode is valid
        """
        # Checks length of postcode
        if len(postcode) < 5 or len(postcode) > 8: 
            return False

        # Convert to letters and digits to check if postcode is valid
        formatted_postcode = Formatter.convert_postcode(postcode)
        is_valid = formatted_postcode in Formatter.get_postcode_formats()
        if is_valid is False:
            return False
        
        # Check correct letters used
        is_valid = Validator.postcode_letter_checker(postcode, formatted_postcode)
        if is_valid is False:
            return False
        
        return True
        
    
    @staticmethod
    def retrieve_details(postcode):
        """
        Retrieves details relating to an entered postcode if it is valid, 
        by breaking down it's parts into:

        Outward code:
            - Area
            - District

        Inward code:
            - Sector
            - Unit
        """
        is_postcode_valid = Validator.validate(postcode)
        if is_postcode_valid is False: 
            return "Postcode is invalid. No data can be retrieved. Please enter a valid postcode.\n"
        
        # Separate outward_code from the inward_code by using the space as the 
        # divider
        outward_code, inward_code = postcode.split(" ")

        area = Formatter.get_postcode_area(outward_code)
        district = Formatter.get_postcode_district(outward_code)
        sector = Formatter.get_postcode_sector(inward_code)
        unit = Formatter.get_postcode_unit(inward_code)

        postcode_details = {"area": area, "district": district, "sector": sector, "unit": unit}

        return "Postcode details: " + str(postcode_details) + "\n"
    
    @staticmethod
    def postcode_letter_checker(postcode, formatted_postcode):
        """
        Checks if letters are correct at certain postcode positions
        """
        # First position check
        first_position_excluded_letters = ('Q', 'V', 'X')
        if postcode[0] in first_position_excluded_letters: return False

        # Second position check
        second_position_excluded_letters = ('I', 'J', 'Z')
        if postcode[1] in second_position_excluded_letters: return False

        # Third position check
        if formatted_postcode.startswith("A9A"):
            third_position_allowed_letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'P', 'S', 'T', 'U', 'W')
            if postcode[2] not in third_position_allowed_letters: return False

        # Fourth position check
        if formatted_postcode.startswith("AA9A"):
            fourth_position_allowed_letters = ('A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y')
            if postcode[3] not in fourth_position_allowed_letters: return False

        # Final two letters check
        final_letters_to_exclude = ('C', 'I', 'K', 'M', 'O', 'V')
        if postcode[-2] in final_letters_to_exclude or postcode[-1] in final_letters_to_exclude:
            return False
        
        return True