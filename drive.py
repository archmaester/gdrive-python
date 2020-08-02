import os
import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import chdir, listdir, stat

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(
        description='API for managing Google drive')
    parser.add_argument(
        '--generate-cred', dest='generate_cred', help='Generates creds.txt',
        action='store_true')
    parser.add_argument(
        '--upload-file', dest='upload_file', help='Uploading file to Google Drive',
        action='store_true')
    parser.add_argument(
        '--upload-folder', dest='upload_folder', help='Uploading folder to Google Drive',
        action='store_true')
    parser.add_argument(
        '--parent-id', dest='parent_id', help='Id of the parent folder',
        default='', type=str)
    parser.add_argument(
        '--file-name', dest='file_name',
        help='title of the file that will be saved',
        default='', type=str)
    parser.add_argument(
        '--folder-name', dest='folder_name',
        help='title of the file that will be saved',
        default='', type=str)
    parser.add_argument(
        '--upload-name', dest='upload_name',
        help='title of the file that will be saved',
        default='', type=str)
    parser.add_argument(
        '--file-path', dest='file_path',
        help='Path of the file where it is to be saved/fetcher',
        default='', type=str)
    parser.add_argument(
        '--folder-path', dest='folder_path',
        help='Path of the file where it is to be saved/fetcher',
        default='', type=str)

    args = parser.parse_args()
    return args


def main():

    args = parse_args()
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(os.environ["DRIVE_SECRET_PATH"])
    drive = GoogleDrive(gauth)

    if args.upload_file:

        file = drive.CreateFile({"title": args.upload_name,
                                 'parents': [{'id': args.parent_id}]})
        file.SetContentFile(os.path.join(args.file_path, args.file_name))
        file.Upload()
        print("You have successfully uploaded the file")

        
    if args.upload_folder:
        
        create_folder(drive, args.folder_name, args.parent_id, args.folder_path)


def create_folder(drive, folder_name, parent_id, folder_path):
    
    folder_metadata = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{"kind": "drive#fileLink", "id": parent_id}]
    }

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    upload_files(drive, folder['id'], folder_path)    


def upload_files(drive, folder_id, folder_path):
    
    for file in os.listdir(folder_path):

        statinfo = stat(os.path.join(folder_path, file))
        if statinfo.st_size > 0:

            print('Uploading :):) ' + file)
            if os.path.isdir(os.path.join(folder_path, file)):
                create_folder(drive, file, folder_id, os.path.join(folder_path, file))
            else:
                f = drive.CreateFile({
                    "title": file,
                    "parents": [{"kind": "drive#fileLink", "id": folder_id}]})
                f.SetContentFile(os.path.join(folder_path, file))
                f.Upload() 
        else:
            print('file {0} is empty :('.format(file))


if __name__ == "__main__":
    main()