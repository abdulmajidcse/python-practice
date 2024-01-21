while True:
    try:
        x = int(input("Please enter a number: "))
        print("Your entered number: {0}".format(x))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    finally:
        # always go there
        print("Number input try-catch closed...")

print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")

try:
    raise NameError("A custom name error")
except NameError:
    print("custom error")
    # if you don't want to handle error, then raise it again
    raise