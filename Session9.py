#Task 1

def calculate_final_price(price, discount_rate):
    discount_amount = price * (discount_rate/100)
    final_price = price - discount_amount
    return final_price

#Task 2

def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'Ahmedabad':
        return 0
    else:
        return 50

#Task 3

def format_price(price, currency='INR'):
    if currency == 'INR':
        return "₹500"
    else:
        return "$500"

#Task 4

def apply_coupon(price, coupon_code=None):
    if coupon_code == 'ZOMATO10':
        discount = price * (10/100)
        final_price = price - discount
        return f"discounted price: {final_price}"
    else:
        return f"original price: {price}"