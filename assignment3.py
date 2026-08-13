#Session 3 Python Practical
#This program demonstartes data types,
#type conversion,functions,input,and boolean values.

#Task 1:Variables and data types

age = 18
height = 175.25
name = "Patel Mohit"
spotify_account = True

print(age)
print(type(age))

print(height)
print(type(height))

print(name)
print(type(name))

print(spotify_account)
print(type(spotify_account))

#Task 2:Calculate total cart amount

prices = ['199.99', '49', '350.75']
def total_cart_amount(prices) :
    total = float(prices[0]) + float(prices[1]) + float(prices[2])
    return total

print(total_cart_amount(prices))

#Task 3:Check Cricket Score

score = int(input("Enter Your Score: "))

if score >= 50 :
    print("Half-Century!")
else:
    print("Keep Going!")

#Task 4 convert string to boolean

is_premium = "True"

is_premium = is_premium == "True"

print("Premium Account:",is_premium)
print("Type:",type(is_premium))