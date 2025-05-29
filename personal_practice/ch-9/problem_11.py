import os

def rename_file():
    old_file_name = "your_file_name.txt"  # The current file name (change this to your file)
    new_file_name = "renamed_by_python.txt"  # The new file name
    
    try:
        # Renaming the file
        os.rename(old_file_name, new_file_name)
        print(f"File has been renamed to '{new_file_name}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{old_file_name}' does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to rename the file
rename_file()
