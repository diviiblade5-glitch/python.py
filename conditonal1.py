name = input("What is your name?: ")
age = input("What is your age?: ")

try:
    age = int(age)

    if age > 100:
        print("Please enter a realistic age")

    elif age < 0:
        print("Please enter a valid age")

    elif age < 18:
        print(f"Oops sorry {name}, can't let you in, you're a minor")

    else:
        print(f"Hello {name}, welcome to the club")

except ValueError:
    print("Enter age in digits only")