#Task 1

song_titles = ["Shape of You","Blinding lights", "Levitating", "Senorita"]

lowercase = lambda song: song.lower()

cleaned_songs = list(map(lowercase, song_titles))

print(cleaned_songs)

#Task 2

ratings = [4.2,3.8,4.5,2.9,3.5]

high_ratings = list(filter(lambda rating: rating> 4.0, ratings))

print(high_ratings)

#Task 3

from functools import reduce

prices = [499,1299,299,799]

total = reduce(lambda x,y: x+y, prices)

print(f"Total price: ₹{total}")

#Task 4

def format_followers(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)

followers = [950, 1500 ,25000, 1200000]

formatted_followers = list(map(format_followers, followers))

print(formatted_followers)

# Task 5

ipl_scores = [101, 98, 120, 77, 88]

even_scores = list(filter(lambda score: score % 2 == 0, ipl_scores))

print(even_scores)