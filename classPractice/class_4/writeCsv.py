import csv

fileName = "student.csv"

def studentData(student, header):
    try:
        with open(fileName, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerow(student)
    except Exception as e:
        print(f"Error occurred while writing data to file: {e}")
        
header = ['name', 'age', 'grade']      
student = ['mohammad', '22', '2023']

studentData(student, header)