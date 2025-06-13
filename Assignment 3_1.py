import math
def perform_math_calculations():
    try:
        num_str = input("Enter a number: ")
        number = float(num_str)

        if number >= 0:
            square_root = math.sqrt(number)
        else:
            square_root = "Cannot calculate square root of a negative number"

        if number > 0:
            natural_logarithm = math.log(number)
        else:
            natural_logarithm = "Cannot calculate natural logarithm for non-positive numbers"

        sine_value = math.sin(number)

        print(f"Square root: {square_root}")
        print(f"Logarithm: {natural_logarithm}")
        print(f"Sine: {sine_value}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

perform_math_calculations()
