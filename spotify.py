from spotdl import Spotdl

def download( music_link, threads ):
    client_id = "CHANGE IT"
    client_secret = "CHANGE IT"

    spotdl = Spotdl( client_id=client_id, client_secret=client_secret, threads= threads,output= "./musics" )

    songs = spotdl.search( music_link )

    results = spotdl.download_songs( songs )
    song_names = []
    song, path = spotdl.download( songs[ 0 ] )
    song_names.append( f"{ song.artist } - { song.name }" )
