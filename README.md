# google-drive-manager
Lets you upload files and folders to google drive assuming one has registered on developers.google and has client_secrets.json

#### Prerequisites
- After downloading the client_secrets.json do

```
export DRIVE_SECRET_PATH = $FILEPATH_TO_SECRETS.json'
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

#### Script for uploading a folder

```
python drive.py --upload-folder --parent-id $DRIVE_FOLDER_ID --folder-name $UPLOADNAME --folder-path $FOLDERPATH
```

#### References

- https://medium.com/analytics-vidhya/pydrive-to-download-from-google-drive-to-a-remote-machine-14c2d086e84e

## To Do List
- Updating settings.yaml
- Allow download of files
