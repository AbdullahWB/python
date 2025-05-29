from psutil import *

def list_processes():
    for proc in process_iter(['pid', 'name']):
        print(proc.info)

list_processes()