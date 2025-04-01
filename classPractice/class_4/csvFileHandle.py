import csv

fileName = "./hsk4.csv"
def read_student():
    with open(fileName, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"hanjie: {row[0]}, phinin: {row[1]}, meaning: {row[2]}")
            
read_student()