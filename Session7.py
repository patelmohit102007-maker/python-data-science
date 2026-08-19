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

units = int(input("Enter the number of electricity units consumed: "))

if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = units * 7
elif units <= 300:
    bill_amount = units * 10
else:
    bill_amount = units * 15

print("Your electricity bill amount is:", bill_amount)

#Task 5

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")