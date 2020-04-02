import re
import os

def songConverter(songName, songPath):
    os.system("ffmpeg -i " + "\"" + songPath + '/' + songName + "\"" + " -c:a aac -b:a 192k" + " " + "\"" + songPath + '/' + songName + "\"")