class FileAccessError(Exception):
    pass

def fileS(fileName):
    try:
        with open(fileName, 'r') as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        raise FileAccessError(f"Error occurred while accessing file: {fileName}.")

fileName = input("filename: ")

fileS(fileName)

# try:
#     with open(fileName, 'r') as f:
#         data = f.read()
#         print(data)
# except FileAccessError:
#     raise(FileAccessError)