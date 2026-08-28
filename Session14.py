#Task 1

file = open("Playlist.txt", "w")
file.write("Breaking The Habit\n")
file.write("Stricken\n")
file.write("This is how you remind me\n")
file.write("Buried Alive\n")
file.write("Mr Brightside\n")

file.close()

#Task 2

file = open("Playlist.txt", "r")

for song in file:
    print(song.strip().upper())

file.close()

#Task 3

import csv

file = open("ipl_matches.csv", "r")

reader = csv.DictReader(file)

for match in reader:
    print(match["winner"])

file.close()

#Task 4

import json

file = open("movies.json", "r")

movies = json.load(file)

for movie in movies:
    print(f"{movie['title']} - {movie['rating']}")

file.close()

#Task 5

from pathlib import Path
import json

file_path = Path("my_fav_apps.json")

if not file_path.exists():
    apps = [
        {
            "name": "Discord",
            "category": "Social Media"
        },
        {
            "name": "Zomato",
            "category": "Food Delivery"
        },
        {
            "name": "Phonepe",
            "category": "Finance"
        }
    ]

    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)