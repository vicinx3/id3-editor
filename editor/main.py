import os
import glob
from converter import songConverter

def Main():
    #Retrieves the path to folder with songs
    currentPath =  os.path.abspath(os.path.dirname(__file__))
    songPath = os.path.join(currentPath, "../songs")

    #Iterates files in song folder to tag all songs
    for song in os.listdir(songPath):
        songConverter(song, songPath)

if __name__ == "__main__":
    Main()