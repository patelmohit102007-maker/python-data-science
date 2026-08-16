#Task 1

insta_followers = {
    "John_Cena": 20000000,
    "TheRock": 300000000,
    "Randy_Orton": 10000000,
    "The_Great_khali": 12000000,
    "Cm_Punk": 7000000
}

print(insta_followers)

#Task 2

insta_followers["Virat_Kohli"] = 15000000
insta_followers["TheRock"] = 31000000
del insta_followers["Cm_Punk"]
print(insta_followers)

#Task 3

food_prices = {
    "Pizza": 250,
    "Burger": 180,
    "Biryani": 300,
    "Dosa": 120,
    "Pasta": 220
}

for item, price in food_prices.items():
    if price > 200:
        print(item, price)

#Task 4

flipkart_users = {"mayur", "rahul", "amit", "rohan", "jay"}

myntra_users = {"rahul", "jay", "kunal", "vivek", "amit"}

common_users = flipkart_users.intersection(myntra_users)

print(common_users)

#Task 5

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1={"Linkin_Park","Eminem","Maroon_5"}
playlist2={"Pitbull","Avenged_Sevenfold","The Weeknd"}

unique_artists=get_unique_artists(playlist1,playlist2)

print("Unique Artists:")
print(unique_artists)