import re

# ----------------------------------------------------------------------------------------------------
# This code receives a string and extracts a list of video ids
# ----------------------------------------------------------------------------------------------------

def extractIDS(string):
  # print(re.findall(r'/watch\?v=.{11,11}', cadena))
  video_ids = re.findall(r'/watch\?v=(.{11})', string)  # Stores a list with the ids of the videos

  # Eliminates the repeated results
  actual = ""
  cont = 1
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
  return video_ids
