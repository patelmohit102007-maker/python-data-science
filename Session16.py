#Task 1

food_apps = ["Uber Eats", "DoorDash", "Grubhub", "Postmates", "Seamless"]
app_iterator = iter(food_apps)
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))

#Task 2

def playlist_generator(songs):
    for song in songs:
        yield song

songs = ["Before i forget","stricken","Riot","Payphone","Airplanes"]

playlist = playlist_generator(songs)
print(next(playlist))
print(next(playlist))
print(next(playlist))
print(next(playlist))
print(next(playlist))

#Task 3

shopping_cart = ["Apples", "Bananas", "Oranges", "Grapes", "Mangoes"]

for index,item in enumerate(shopping_cart, start=1):
    print(f"Item {index}: {item}")

#Task 4

teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Sunrisers Hyderabad"]
points = [18, 16, 15, 14]

for team, point in zip(teams, points):
    print(f"Team: {team}, Points: {point}")

#Task 5

def order_id_generator():
    order_id = 1001

    while True:
        yield order_id
        order_id += 1

orders = order_id_generator()

print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))