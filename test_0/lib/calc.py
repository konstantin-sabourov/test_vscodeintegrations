def get_sum(num1, num2):
    """
    Calculate the sum of two numbers.

    Args:
        num1: First number (int or float)
        num2: Second number (int or float)

    Returns:
        The sum of num1 and num2

    Raises:
        TypeError: If either argument is not numeric
    """
    # Check if both arguments are numeric
    if not isinstance(num1, (int, float)):
        raise TypeError(f"First argument '{num1}' is not numeric")

    if not isinstance(num2, (int, float)):
        raise TypeError(f"Second argument '{num2}' is not numeric")

    # Calculate the sum
    result = num1 + num2

    # Print the result
    print(f"Sum of {num1} and {num2} is {result}")

    return result
