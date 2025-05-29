from os import *

def create_process():
    print("Current Process ID:",getpid())
    print("Parent Process ID:",getppid())
    
create_process()
