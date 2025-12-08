sapa_slices=4
small_money_slices=6
big_boys_slices=8
odogwu_slices=12
sapa_prices=2000
small_money_prices=2400
big_boys_prices=3000
odogwu_prices=4200
number_of_people=int(input(""" Welcome to Iya Scambirah Pizza joint!!!!
What is the number of People?\n"""))
pizza_type=(input("""We have:
Sapa Size
Small money
Big Boys
Odogwu
What type of pizza do you want to order Sir/Ma?\n
"""))

pizza_slices=0
pizza_prices=0


if pizza_type.lower() == "sapa size" :
    pizza_slices=sapa_slices
    pizza_prices=sapa_prices
elif pizza_type.lower() == "small money" :
    pizza_slices=small_money_slices
    pizza_prices=small_money_prices
elif pizza_type.lower() == "big boys" :
    pizza_slices=big_boys_slices
    pizza_prices=big_boys_prices
elif pizza_type.lower() == "odogwu" :
    pizza_slices=odogwu_slices
    pizza_prices=odogwu_prices



boxes=1
while boxes * pizza_slices < number_of_people:
    boxes+=1
    pizza_bill=boxes * pizza_prices
    leftover_pizza=boxes * pizza_slices - number_of_people






print("The number of boxes to buy=", boxes , "boxes")
print("Number of left over slices after serving=", leftover_pizza , "slices")
print("Prices", pizza_bill)

