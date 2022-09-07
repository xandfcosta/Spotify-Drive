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
        folder = self.drive.CreateFile( { "title" : self.folder_name, "mimeType": "application/vnd.google-apps.folder" } )
        folder.Upload( )

        filenames = [f for f in os.listdir( ) ]
        for file in filenames:
            if ".mp3" in file:
                file_drive = self.drive.CreateFile( {"name" : f"{ file }", "parents": [ { "kind": "drive#fileLink", "id": folder[ "id" ] } ] } )
                file_drive.SetContentFile( file )
                file_drive.Upload( )
                del file_drive
                os.remove( file )