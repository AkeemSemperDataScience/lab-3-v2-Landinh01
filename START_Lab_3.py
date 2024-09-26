
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
     
    if number < cutoff:
        print(f"{number} is less than {cutoff}")
        return True
    else:
        print(f"{number} is not less than {cutoff}")
        return False
    pass

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float

     # Check if the input is specifically a float
    if isinstance(decimal_number, float):
        # Check if the number is zero
        if decimal_number == 0:
            return "zero"
        # Check if the number is positive
        elif decimal_number > 0:
            return "positive"
        # If the number is not positive or zero, it must be negative
        else:
            return "negative"
    
    # Return "invalid" if the input is not a float
    elif isinstance(decimal_number, int):
        return "invalid"
    # Handle any other type as invalid
    else:
        return "invalid"

    pass

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number.
    
    # Check if the input is an integer and is a positive year number
    if not isinstance(year, int) or year <= 0:
        return "invalid"
    
    # Determine the century or ancient based on the year
    if 2001 <= year <= 2100:
        return "21st century"
    elif 1901 <= year <= 2000:
        return "20th century"
    elif 1801 <= year <= 1900:
        return "19th century"
    elif year < 1801:
        return "ancient"
    else:
        return "invalid" 
    pass

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    
    # Check if all inputs are numbers (int or float)
    if not all(isinstance(i, (int, float)) for i in [number_1, number_2, number_3]):
        return None
    
    # Return the largest of the three numbers
    return max(number_1, number_2, number_3)

    pass

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    # Check if temperature is a number and scale_used is either "C" or "F"
    if not isinstance(temperature, (int, float)) or scale_used not in ["C", "F"]:
        return "Invalid"
    
    # Determine the state of water based on the temperature and scale
    if scale_used == "C":
        if temperature <= 0:
            return "Solid"
        elif 0 < temperature < 100:
            return "Liquid"
        else:
            return "Gas"
    elif scale_used == "F":
        if temperature <= 32:
            return "Solid"
        elif 32 < temperature < 212:
            return "Liquid"
        else:
            return "Gas"
    pass

