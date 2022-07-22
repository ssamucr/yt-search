import urllib.request
from extract_ids import extract_ids
import pywhatkit
import re

# ----------------------------------------------------------------------------------------------------
# This code receives a key word to search, open the default browser and play the first occurrence
# ----------------------------------------------------------------------------------------------------

# Receives the keyword to search
search_keyword = re.sub(" ", "+", input("Texto a buscar: "))

# Create a http.client.HTTPResponse object with the results info
html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_keyword}")

# Convert the object to a string
string = html.read().decode()

video_ids = extract_ids(string)

pywhatkit.playonyt(f"https://www.youtube.com/watch?v={video_ids[0]}")  # Searches the first result
