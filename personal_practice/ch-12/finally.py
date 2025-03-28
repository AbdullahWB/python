def main():
    try:
        a = int(input("Enter a number: "))
        print(f"The square of {a} is: {a**2}")
        return
    except ValueError as v:
        print(f"Invalid input. Please enter a number. {v}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Program completed successfully.")
        
main() # finally is very important in function