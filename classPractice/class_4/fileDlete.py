import os

def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' has been deleted successfully.")
    except FileNotFoundError as e:
        print(f"File '{filename}' does not exist.", e.message)
        
print("do you want to delete file")
cond = input("Are you sure you want to delete yes/not: ")

if cond.lower() == 'yes':
    filename = input("Enter the filename you want to delete: ")
    deleteFile(filename)
elif cond.lower() == 'not':
    print("Operation cancelled.")
else:
    print("Operation cancelled.")