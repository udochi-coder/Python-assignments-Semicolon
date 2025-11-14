age=int(input("Enter your age: "))

heartrate=220 - age
print("Your maximum heart rate is  " , heartrate)
range_heart_rate_One= heartrate * 0.5
range_heart_rate_Two= heartrate * 0.8
print("Your target heart rate is  " , range_heart_rate_One ,"-",range_heart_rate_Two)

