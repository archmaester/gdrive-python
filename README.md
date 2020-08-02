# GoogleDrive Python API
Lets you upload files and folders to google drive assuming one has registered on developers.google and has client_secrets.json

#### Instructions
- After downloading the client_secrets.json do

```
export DRIVE_SECRET_PATH=$FILEPATH_TO_SECRETS.json
```

- Rename settings_template.yaml to settings.yaml
- Copy clientId and clientSecret from client_secrets.json to respective fields in settings.yaml
- It will ask for one time verification, for subsequent runs, the parameters will be taken from creds.json
- If you are running on a server where verification on browser is not possible, create a ssh tunnel

```
ssh -N -L localhost:$MACHINE_PORT_NO:localhost:$SERVER_PORT_NO username@server-ip
```

#### Script for uploading a file 

```
python drive.py --upload-file --parent-id $DRIVE_FOLDER_ID --file-name $FILENAME --upload-name $UPLOADNAME --file-path $DIRPATH
```

- **DRIVE_FOLDER_ID**: Id that you will find on the url for the parent-folder where you want to upload a new file
- **FILENAME**: name of the file you want to upload
- **DIRPATH**: Path to directory where the file is
- **UPLOADNAME**: Name of the file that will appear on drive

#### Script for uploading a folder

```
python drive.py --upload-folder --parent-id $DRIVE_FOLDER_ID --folder-name $UPLOADNAME --folder-path $FOLDERPATH
```

- **DRIVE_FOLDER_ID**: Id that you will find on the url for the parent-folder where you want to upload a new folder
- **UPLOADNAME**: name of the folder to be uploaded that will appear on the drive
- **FOLDERPATH**: Path to the folder which you want to upload

#### References

- https://medium.com/analytics-vidhya/pydrive-to-download-from-google-drive-to-a-remote-machine-14c2d086e84e

## Done List

- ✅  Recursively upload folders and files
- ✅  Add settings.yaml
- ✅  No verification for subsequent runs
- ✅  Upload file 
- ✅  Upload folder

## To Do List

- ⬜️  Script to download files
- ⬜️  Script to list files in a folder
- ⬜️  Script to update files
- ⬜️  Script to delete files
