def factorial(n):

    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # Factorial of 0 is 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    fact_result = factorial(num)

    if isinstance(fact_result, int):
        print(f"Factorial of {num} is: {fact_result}")
    else:
        print(fact_result)

except ValueError:
    print("Invalid input. Please enter an integer.")