
print("Welcome to the Bonus Tip Calculator")
Total_Bill = input("What is the total bill?: $")

Number_of_People = input("How many people are going to share the bill?: ")

Bill_for_each = float(Total_Bill) / float(Number_of_People)


Tip_Percentage = input("What percentage tip would you like to give?: ")

Tip = (100 + float(Tip_Percentage))/100

Tip_for_each = Bill_for_each * Tip


print(f"Total amount with tip each person should give is {round(Tip_for_each, 2)}, thank you for being generous. ")
