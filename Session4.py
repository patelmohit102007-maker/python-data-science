#Task 1

product = "Flipkart-Sale2024"
print(product.lower().replace("-", " "))

#Task 2

product_name = " OnePlus Nord-CE 3 "
print(product_name.strip().upper().replace("-", ":"))

#Task 3

product_code = "ZOMATO-FOOD-2024"

def split_product_code(product_code):
    return product_code.split("-")

print(split_product_code(product_code))

#Task 4

product = "Spotify_Premium_Offer"
print(product[8:15])

#Task 5

product = "Myntra Shirt"
price = 799.5

print(f"Deal: {product} is available at ₹{price:.2f} only!")