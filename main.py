import urllib.request
import re
import pywhatkit

# ----------------------------------------------------------------------------------------------------
# This code receives a key word to search, open the default browser and searches the first occurrence
# ----------------------------------------------------------------------------------------------------

# Receives the keyword to search
search_keyword = re.sub(" ", "+", input("Texto a buscar: "))

# Create an http.client.HTTPResponse object with the results info
html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_keyword}")

# Convert the object to a string
string = html.read().decode()

# print(re.findall(r'/watch\?v=.{11,11}', cadena))
video_ids = re.findall(r'/watch\?v=(.{11,11})', string)  # Stores a list with the ids of the videos

# Eliminates the repeated results
for x in range(len(video_ids)):
    if x == 0:
        actual = video_ids[x]
        cont = 1
    elif actual == video_ids[x]:
        limit = x
    elif actual != video_ids[x]:
        actual = video_ids[x]
        video_ids[cont] = actual
        cont += 1

video_ids = video_ids[0:cont]  # Stores the unrepeated results

pywhatkit.playonyt(f"https://www.youtube.com/watch?v={video_ids[0]}")  # Searches the first result
