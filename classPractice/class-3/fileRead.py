file_name = "file.txt"

def read_file(file_path):
    print(f"Reading from file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            # content = file.read()
            content2 = file.readline()
            # content4 = file.readline()
            # content3 = file.readlines()
            print("File content:")
            print(content2)
            # print(content4)
            # print(content)
            # while True:
            #     print(content2)
            #     if content2 == "":
            #         break
            # print(content3[1])
            # for line in content3:
            #     print(line)
            # print(content3[0])
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error Occurred: {e}")
        
        
# with open(file_name, 'w') as file:
#     content = file.write("hello world!")


read_file(file_name)