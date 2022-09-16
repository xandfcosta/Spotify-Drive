from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import shutil

class Upload( ):
    def __init__( self, folder : str ) -> None:
        self.drive = GoogleDrive
        self.folder_name = folder

        self.authenticate( )
        self.upload( )
        
    def authenticate( self ):
        gauth = GoogleAuth( )
        gauth.LoadCredentialsFile( "mycreds.txt" )

        if gauth.credentials is None:
            gauth.LocalWebserverAuth( )
        elif gauth.access_token_expired:
            gauth.Refresh( )
        else:
            gauth.Authorize( )

        gauth.SaveCredentialsFile( "mycreds.txt" )
        self.drive = GoogleDrive( gauth )

    def upload( self ):     
        # file_list = self.drive.ListFile( { 'q': "'root' in parents and trashed=false" } ).GetList( )
        # folder_exists = False
        
        # for file in file_list:
        #     if file["title"] == "Spotify-Drive":
        #         folder_main = file
        #         folder_exists = True
        #         break
            
        # if not folder_exists:
        #     folder_main = self.drive.CreateFile( { "title" : "Spotify-Drive", "mimeType": "application/vnd.google-apps.folder" } )
        #     folder_main.Upload( )
        
        folder = self.drive.CreateFile( { "title" : self.folder_name, "mimeType": "application/vnd.google-apps.folder" } )
        folder.Upload( )
        
        os.chdir( "./musics")
        
        filenames = [ f for f in os.listdir( ) ]
        for file in filenames:
            file_drive = self.drive.CreateFile( {"name" : f"{file}", "parents": [ { "kind": "drive#fileLink", "id": folder[ "id" ] } ] } )
            file_drive.SetContentFile( file )
            file_drive.Upload( )
            del file_drive
        
        os.chdir( "..")
        shutil.rmtree( "./musics" )