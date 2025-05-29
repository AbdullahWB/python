# import os
# print("CALLER PID:", os.getpid())
# command = ["python3", "called.py"]
# os.execvp(command[0], command)

import os

command = 'pwd'
agruments = ['pwd']

try:
    os.execvp(command, agruments)
except FileNotFoundError:
    print(f'Error: The command "{command}" was not found.')
except:
    print('An error occurred.')