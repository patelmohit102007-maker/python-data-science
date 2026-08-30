#Task 1

def get_song_duration_per_minute(total_duration,number_of_songs):
    try:
        average_duration = total_duration/number_of_songs
        return average_duration
    
    except ZeroDivisionError:
        return "Cannot calculate average: playlist has zero songs."

    finally:
        print("Calculation completed.")

print(get_song_duration_per_minute(240,10))
print(get_song_duration_per_minute(240,0))

#Task 2

def price_per_item(total_amount, item_count):
    try:
        price = total_amount/item_count
        print(f"Price per item: ₹{price}")

    except ZeroDivisionError:
        print("Cannot Calculate price: item cannot be zero.")

total_amount = float(input("Enter total cart amount: ₹"))
item_count = float(input("Enter number of item: "))

print(price_per_item(total_amount,item_count))

#Task 3

class NooffersApplied(Exception):
    pass

def cashback_calculator(total_spend, number_of_offers):
    try:
        if number_of_offers == 0:
            raise NooffersApplied("No offers were applied.")

        average_cashback = total_spend / number_of_offers
        print(f"Average cashback per offer: ₹{average_cashback}")

    except NooffersApplied as error:
        print(f"Error: {error}")

total_spend = float(input("Enter your total spend: ₹"))
number_of_offers = int(input("Enter number of offers applied: "))

cashback_calculator(total_spend, number_of_offers)

#Task 4

def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews

    except ZeroDivisionError:
        return "Cannot calculate average rating: number of reviews cannot be zero."

    finally:
        print("Thank you for using the calculator")


print(calculate_average_rating(500, 0))

#Task 5

def safe_divide_for_zomato(bill_amount, number_of_people):
    try:
        amount_per_person = bill_amount / number_of_people

    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")

    else:
        print(f"Amount per person: ₹{amount_per_person}")

    finally:
        print("Split calculation done")


safe_divide_for_zomato(2000, 4)
safe_divide_for_zomato(2000, 0)