numberOne=int(input("Enter first number: "))
numberTwo=int(input("Enter second number: "))
numberThree=int(input("Enter third number: "))

sum=numberOne + numberTwo + numberThree
print("The sum is " , sum)
average= sum / 3
print("The average is " , average)
product=numberOne * numberTwo * numberThree
print("The Product is " , product) 

if(numberOne > numberTwo and numberOne > numberThree):
 print("The largest number is " , numberOne)
if(numberOne < numberTwo and numberOne < numberThree):
 print("The lowest number is " , numberOne)
if(numberTwo > numberThree and numberTwo > numberOne):
 print("The largest number is " , numberTwo)
if(numberTwo < numberThree and numberTwo < numberOne):
 print("The lowest number is " , numberTwo)
if(numberThree > numberTwo and numberThree > numberOne):
 print("The largest number is " , numberThree)
if(numberThree < numberTwo and numberThree < numberOne):
 print("The lowest number is " , numberThree)

















