def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

# Example usage:
print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print error message
