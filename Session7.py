#Task 1

listening_time = 246
if listening_time > 120:
    print("You are true music fan!")
else:
    print("keep listening")

#Task 2

order_amount = int(input("Enter your zomato order amount: "))
if order_amount > 300:
    print("You are eligible for free delivery!")
else:
    print("delivery charges will be applied")

#Task 3

cart_total = int(input("Enter your cart total amount: "))
if cart_total > 2000:
    print("You are eligible for 10% discount!")
elif cart_total > 1000:
    print("You are eligible for 5% discount!")
else:
    print("No discount available")

#Task 4

points = int(input("Enter your IPL fantasy team points: "))

if points > 800:
    print("champion!")
else:
    if points >= 500:
        print("Top performer!")
    else:
        print("Keep Trying!")