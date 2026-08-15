#Task 1
playlist_ids = [101, 205, 309, 412, 518]
print(playlist_ids)

#Task 2

playlist_ids.append(620)
playlist_ids.extend([721, 823])
print(playlist_ids)

#Task 3

removed_song = playlist_ids.pop()
print(f"Removed song ID: {removed_song}")
print(f"Remaining playlist IDs: {playlist_ids}")

#Task 4

insta_filters = ("Clarendon", "Gingham", "Moon", "Lark")
insta_filters[0] ="Lark" #Tuples are immutable, so this will raise an error

#Task 5

recent_orders = ["Order1", "Order2", "Order3"]
# List is used because recent orders can be added or removed.

ipl_teams = ("CSK", "MI", "RCB", "KKR")
# Tuple is used because the IPL team names are fixed and should not change.