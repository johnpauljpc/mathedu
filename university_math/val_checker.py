from django.contrib import messages
def check_number(user_input=None):

    # Check if the input is an integer
    if user_input.isdigit():
        integer_value = int(user_input)
        return integer_value
    else:
        try:
            float_value = float(user_input)
            return float_value
            # Input is a floating-point number
            # Do something with float_value
        except:
            return False
            # Input is not a number
            # Handle the case where the input is not a number
