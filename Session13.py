#Task 1

def print_playlist_songs(songs):
    if len(songs) == 0:
        return

    print(songs[0])
    print_playlist_songs(songs[1:])

songs = ["All of the lights", "The diary of jane", "Boulevard of Broken of Dreams", "Bring me to life", "Numb", "Stricken", "Maps"]

print_playlist_songs(songs)

#Task 2

messages = {
    "Family": {
        "count": 5,
        "subgroups": [
            {
                "count": 3,
                "subgroups": []
            },
            {
                "count": 2,
                "subgroups": []
            }
        ]
    },

    "Friends": {
        "count": 4,
        "subgroups": []
    }
}

def count_unread_messages(messages):
    total = 0

    if isinstance(messages, dict):
        groups = messages.values()
    else:
        groups = messages

    for group in groups:
        total += group["count"]
        total += count_unread_messages(group["subgroups"])

    return total


print(count_unread_messages(messages))

#Task 3

x = 'Global'

def outer():
    x = 'Outer'

    def inner():
        nonlocal x
        x = 'inner'

    inner()
    print("Inside outer:", x)

outer()
print("outside:", x)

#Task 4

def format_number_short(n, suffix_index=0):
    suffixes = ["", "K", "M", "B"]

    if n < 1000:
        if suffix_index == 0:
            return str(n)
        return f"{n:.1f}{suffixes[suffix_index]}"

    return format_number_short(n / 1000, suffix_index + 1)

print(format_number_short(1200000))