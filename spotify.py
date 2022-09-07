from spotdl import Spotdl

def download( music_link ):
    client_id = "21122f990feb4a08911a27cf2b8e722c"
    client_secret = "81405a8fd862410e8bc71d89e996b234"

    spotdl = Spotdl( client_id=client_id, client_secret=client_secret )

    songs = spotdl.search( music_link )

    results = spotdl.download_songs( songs )
    song_names = []
    song, path = spotdl.download( songs[ 0 ] )
    song_names.append( f"{ song.artist } - { song.name }" )
