import re
import os

def songConverter(songName, songPath):
    #splits the provided song name into just the name of the song and also the format
    seperated = songName.split(".")
    songNameNoFormat = seperated[0]
    songFormat = seperated[1]

    #Create the output path for converted songs
    currentPath =  os.path.abspath(os.path.dirname(__file__))
    songPathOut = os.path.join(currentPath, "../songsConverted")

    #Use ffmpeg with flags -y to confirm overwrites and the Apples lossless audio codec to output Apple .m4a files and retain metadata across conversion
    os.system("ffmpeg -i " + "\"" + songPath + '/' + songNameNoFormat + "." + songFormat + "\"" + " -vn -y -acodec alac -map_metadata 0 " + " " + "\"" + songPathOut + '/' + songNameNoFormat + ".m4a" + "\"")