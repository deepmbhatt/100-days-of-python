#This is a tip calculator which helps you find the amount of bill a person has to pay while going out in a group.
print("Wecome to the tip calculator")
bill=int(input("What was the total bill?\n"))
tip_percent=int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
n=int(input("How many people to split the bill?\n"))
amount=round((bill*(1+(0.01*tip_percent)))/n,2)
print(f"Each person should pay {amount}")