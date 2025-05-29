def check_for_twinkle():
    try:
        with open('poems.txt', 'r') as file:
            content = file.read().lower()  # Convert to lowercase to avoid case issues
            if 'twinkle' in content:
                print("The word 'twinkle' is present in the file.")
            else:
                print("The word 'twinkle' is not found in the file.")
    except FileNotFoundError:
        print("File 'poems.txt' not found.")

check_for_twinkle()
