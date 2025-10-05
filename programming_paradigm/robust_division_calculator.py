# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides numerator by denominator, handling division by zero and non-numeric inputs.
    Returns either the result or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is {result}"
