from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["chinook"]

tracks = db["tracks"]
albums = db["albums"]
artists = db["artists"]

result = []
for track in tracks.find():
    album = albums.find_one({"AlbumId": track["AlbumId"]})
    if album:
        artist = artists.find_one({"ArtistId": album["ArtistId"]})
        if artist:
            result.append({
                "Track": track["Name"],
                "Album": album["Title"],
                "Artist": artist["Name"]
            })

print("Tracks with Album and Artist:\n")
for item in result:
    print(f"Track: {item['Track']}\nAlbum: {item['Album']}\nArtist: {item['Artist']}\n")
