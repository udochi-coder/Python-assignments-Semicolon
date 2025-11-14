amount=int(input("Enter investment amount"))
annualrate=0.007
nOne=10
nTwo=20
nThree=30

sumamountcalc=1 + 0.007
amountcalc=sumamountcalc ** nOne
amountcalcTwo=sumamountcalc ** nTwo
amountcalcThree=sumamountcalc ** nThree

Totalamountcalc=amount * amountcalc
print("You will have " , Totalamountcalc , "in 10 years")
TotalamountcalcTwo=amount * amountcalcTwo
print("You will have " , TotalamountcalcTwo , "in 20 years")
TotalamountcalcThree=amount *amountcalcThree
print("You will have " , TotalamountcalcThree , "in 30 years")


