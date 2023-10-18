
class NegativeNumberError(Exception):
    pass

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a demoninator: "))

    if n < 0 or d < 0:
        raise NegativeNumberError()

    q = n / d #exception was riased when trying to divide by zero

    print(q)



except ZeroDivisionError:
    print("Denomintor cant be zero")

except ValueError:
    print("Inputs must be Integers")

except NegativeNumberError:
    print("Must be positive integers")

except Exception as e:
    print("Something went wrong")
    print(e)
    # Log Debug information  ( including traceback) to an error log file)



