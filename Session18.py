# Task 1

import re

text = "Call me at +91-9876543210 or +91-9123456789. You can also try 9876543210."

phone_numbers = re.findall(r"\+91-\d{10}", text)

print(phone_numbers)

# Task 2

import re

def check_date(text):
    pattern = r"\d{2}/\d{2}/\d{4}"


    if re.search(pattern, text):
        return True
    else:
        return False

print(check_date("Today's date is 12/05/2023."))
print(check_date("Today's day was quite weird."))

# Task 3

import re

text = "The prices are Rs. 299, Rs. 1500, Rs. 799 and Rs. 250."

prices = re.findall(r"Rs\. (\d+)", text)

prices = [int(price) for price in prices]

total = sum(prices)

print(prices)
print("Total: ", total)

# Task 4

import re

text = "Contact me at mohit2007@gmail.com or council2026@gmail.com for help."

modified_text = re.sub(r"\S+@\S+\.\S+", "[hidden email]", text)

print(modified_text)

# Task 5

import re

with open("instagram_comments.txt", "r") as file:
    text = file.read()

usernames = re.findall(r"@[A-Za-z0-9_]{3,}", text)

unique_usernames = set(usernames)

print(unique_usernames)