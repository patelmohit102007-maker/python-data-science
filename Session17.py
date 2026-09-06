# Task 1

import math

number = 225

square_root = math.sqrt(number)

print(square_root)

# Task 2

import os

folder_path = os.path.join(os.getcwd(), "MyDownloads")

os.makedirs(folder_path, exist_ok=True)

print(os.path.abspath(folder_path))

# Task 3

from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_time)

# Task 4

import playlist_utils

playlist = []

playlist_utils.add_song(playlist, "Back in Black")
playlist_utils.add_song(playlist, "Pretender")
playlist_utils.add_song(playlist, "Till i collapse")

print(playlist)

# Task 5

import requests

print(requests.__version__)