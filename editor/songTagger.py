from mutagen.mp4 import MP4

def songTagger(songName, songPath):
    albumSearchURL = "http://itunes.apple.com/search?entity=album&limit=200&term=kill+this+love"
    songSearchURL = "http://itunes.apple.com/lookup?entity=song&limit=200&id=1458062491"

    songPath = list(songPath)
    songPath = songPath[:len(songPath) - 5]
    songPath = "".join(songPath)
    songPath = songPath + "songsConverted"

    seperated = songName.split(".")
    songName = seperated[0] + ".m4a"

    song = MP4(songPath + "/" + songName)
    print(song.MP4Tags)

