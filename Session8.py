#Task 1

food_apps = ["Uber Eats", "DoorDash", "Grubhub", "Postmates", "Seamless"]
for app in food_apps:
    print(app)

#Task 2

daily_steps = [7500, 6500, 4500, 2000, 8000, 12000, 3000]
day = 0

while day < len(daily_steps):
    if daily_steps[day] > 10000:
        print(f"Day {day + 1} Crossed 10k steps!")
        break

    day += 1

#Task 3

ipl_teams = ["CSK","Mumbai Indians","Rajasthan Royals","GT","Royal Challengers"]

def print_long_team_names(ipl_teams):
    for team in ipl_teams:
        if len(team) >= 6:
            print(team)

print_long_team_names(ipl_teams)

#Task 4

song_durations = [210, 185, 240, 195, 300]

for position, duration in enumerate(song_durations, start=1):
    print(f"Song {position} duration: {duration} seconds")

#Task 5

item_prices = [500, 0, 750, 300, 800, 400]

total = 0

for price in item_prices:

    if price == 0:
        continue

    if total + price > 2000:
        break

    total += price

print(f"Final cart total: ₹{total}")