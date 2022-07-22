import urllib.request
import extract-ids.extractIDS
import pywhatkit

# ----------------------------------------------------------------------------------------------------
# This code receives a key word to search, open the default browser and play the first occurrence
# ----------------------------------------------------------------------------------------------------

# Receives the keyword to search
search_keyword = re.sub(" ", "+", input("Texto a buscar: "))

# Create a http.client.HTTPResponse object with the results info
html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_keyword}")

# Convert the object to a string
string = html.read().decode()

video_ids = extractIDS(string)

pywhatkit.playonyt(f"https://www.youtube.com/watch?v={video_ids[0]}")  # Searches the first result
