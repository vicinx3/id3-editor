import os
import glob
from converter import songConverter
from songTagger import songTagger

def tagger():
    #Retrieves the path to folder with songs
    currentPath =  os.path.abspath(os.path.dirname(__file__))
    songPath = os.path.join(currentPath, "../songs")

    #Iterates files in song folder to tag all songs
    for song in os.listdir(songPath):
        songConverter(song, songPath)
        songTagger(song, songPath)
        
tagger()