import dropbox, os.path

class TransferData:

    def upload_file(self, relative_path, dropbox_path,):
        self.relative_path = relative_path
        self.dropbox_path = dropbox_path

        for root, dirs, files in os.walk(file_from):

        relative_path = os.path.relpath (local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

        with open (local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

    if __name__ == '__upload_file__':
     upload_file()
   

def main():
    relative_path = 'sl.B2jRw9Dhd5dF6-2xHEVR8kbW8aSFNvYAmfZkl44-vQNK_CuxeVs6DhKAOzdnVx8hWzakLLZUvNOs5Iex-gofAFJha4IU3b0cPNkMP_cCGYlSuA33D94UJYTsgZTs2zSSEbBhuqpGB0zi'
    transferData = TransferData(relative_path)

    file_from = input("User, enter the file path to transfer")
    file_to = input("Enter the full path to upload the dropbox") 

    # API v2
    transferData.upload_file(file_from, file_to)
    print ("File is successfully uploaded")

if __name__ == '__main__':
    main()      