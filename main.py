import multiprocessing
import spotify
from drive import Upload

def main( ):
    with open( "configs.txt" ) as file:
        musics = file.readlines()
        musics = [line.rstrip() for line in musics]
    
    folder_name = musics[ 0 ]
    musics.pop( 0 )

    spotify.download( musics, threads= multiprocessing.cpu_count() )

    Upload( folder= folder_name )

if __name__ == "__main__":
    main()