import spotify
from drive import Upload

def main( ):
    folder_name = input( "Playlist name: " )

    music = []
    
    link = input( "Link: " )
    music.append( link )

    spotify.download( music )

    Upload( folder= folder_name )

if __name__ == "__main__":
    main()