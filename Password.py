number=input("Enter your password: ")

numbers = len(number)

if numbers  > 6 and numbers <= 10:
    print("Medium")
if( numbers < 6 ):
    print("Weak")
if( numbers > 10):
    print("Strong")
if(numbers  < 1):
     print("is invalid")



