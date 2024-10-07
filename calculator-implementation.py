def validate_inputs(expression):
    try:
        # Check if the expression contains valid operators and numbers
        allowed_chars = set("0123456789+-*/() ")
        if not all(char in allowed_chars for char in expression):
            return False
        # Test if the expression can be evaluated
        eval(expression)
        return True
    except:
        return False

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None

def validate_results(result):
    # Check if result is a valid number and not too large/small
    return result is not None and isinstance(result, (int, float)) and -1e308 <= result <= 1e308

def main():
    while True:
        print("\nCalculator")
        print("Enter an expression (or 'q' to quit)")
        
        # User enters calculation
        user_input = input("Enter calculation: ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        # Validate inputs
        if not validate_inputs(user_input):
            print("Error: Invalid input. Please use numbers and operators (+, -, *, /)")
            continue
        
        # Perform calculation
        result = calculate(user_input)
        
        # Validate results
        if not validate_results(result):
            print("Error: Invalid result. Please check your input and try again.")
            continue
        
        # Display results
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
