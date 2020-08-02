# google-drive-manager
Lets you upload files and folders to google drive assuming one has registered on developers.google and has client_secrets.json

#### Prerequisites
After downloading the client_secrets.json do 
export DRIVE_SECRET_PATH = $FILEPATH_TO_SECRETS.json

generate mycreds and set
export DRIVE_CRED_PATH = $FILEPATH_TO_mycreds

Currently uses port 8080 for receving signals, update it as per your json

#### Script for uploading a file 
python drive.py --upload-file --parent-id $DRIVE_FOLDER_ID --file-name $FILENAME --upload-name $UPLOADNAME --file-path $DIRPATH

#### Script for uploading a folder
python drive.py --upload-folder --parent-id $DRIVE_FOLDER_ID --folder-name $UPLOADNAME --folder-path $FOLDERPATH

#### References
- https://medium.com/analytics-vidhya/pydrive-to-download-from-google-drive-to-a-remote-machine-14c2d086e84e
## To Do List
- Updating settings.yaml
- Allow download of files
