number=int(input("Enter five digit integer: "))

numberOne=number // 10000
numberTwo=(number // 1000) % 10
numberThree=(number // 100) % 10
numberFour=(number // 10) % 10
numberFive=number  % 10
print(f"{numberOne}  {numberTwo}  {numberThree}  {numberFour}  {numberFive}" )


