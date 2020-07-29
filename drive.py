import os
import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(
        description='API for managing Google drive')
    parser.add_argument(
        '--upload', dest='upload', help='Uploading file to Google Drive',
        action='store_true')
    parser.add_argument(
        '--parent-id', dest='parent_id', help='Id of the parent folder',
        default='', type=str, required=True)
    parser.add_argument(
        '--file-name', dest='file_name',
        help='title of the file that will be saved',
        default='', type=str, required=True)
    parser.add_argument(
        '--upload-name', dest='upload_name',
        help='title of the file that will be saved',
        default='', type=str, required=True)
    parser.add_argument(
        '--file-path', dest='file_path',
        help='Path of the file where it is to be saved/fetcher',
        default='', type=str, required=True)

    args = parser.parse_args()
    return args


def main():

    args = parse_args()
    gauth = GoogleAuth()

    gauth.LoadClientConfigFile(os.environ["DRIVE_SECRET_PATH"])
    gauth.LoadCredentialsFile(os.environ["DRIVE_CRED_PATH"])
    drive = GoogleDrive(gauth)

    if args.upload:

        file = drive.CreateFile({"title": args.upload_name,
                                 'parents': [{'id': args.parent_id}]})
        file.SetContentFile(os.path.join(args.file_path, args.file_name))
        file.Upload()
        print("You have successfully uploaded the file")


if __name__ == "__main__":
    main()
