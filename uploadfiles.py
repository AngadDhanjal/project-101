import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    data = f.read()
                    self.dbx.files_upload(data, dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BcfNP-_lrohXXkjX8riDlXfi4LZN4fzwhMxcT8Ij7X7hap54rspnwXqhdBBZS5HnPCbJm1i7nEsuGPiuv2d3GITd9T_0TQPMAPxC8Pj8TBuGCX5KmFkgwDXevQkuIpQkPD-kK8Q'
    transfer_data = TransferData(access_token)

    file_from = str(input("Enter the file path to upload: "))
    file_to = input("Enter the full path to upload to (including filename): ")

    transfer_data.upload_file(file_from, file_to)
    print("File has been uploaded to Dropbox.")

if __name__ == '__main__':
    main()






