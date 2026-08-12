#this variable stores the price of the item
item_price = 250
#this variable stores the delivery fee
delivery_fee = 50
#this variable stores the coupon discount
coupon_discount = 30
#this prints the price of the item, delivery fee, and coupon discount
print("item price:", item_price)
print("delivery fee:", delivery_fee)
print("coupon discount:", coupon_discount)

"""

this checks the item price.
if the item price is greater than 1000, it is eligible for free delivery.
if the item price is less than or equal to 1000, delivery charges apply.

"""
if item_price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")

#this variable stores the team name
team_name = "Gujarat Titans"
#this variable stores the runs scored by the team
runs_scored = 159
#this variable stores the overs played by the team
overs_played = 17

print("Team Name:", team_name)
print("Runs Scored:", runs_scored)
print("Overs Played:", overs_played)