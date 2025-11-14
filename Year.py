number = int(input("Enter year: "))

if number % 4 == 0:
    print("it is a leap year")
elif number % 100 != 0:
    print("it is not a leap year")
elif number % 400 == 0:
    print("it is a leap year")
