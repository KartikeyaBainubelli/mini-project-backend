text = ""

with open("student-record-manager/students.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
    text = [string.strip() for string in text]

arr = [int(s.split(",")[0]) for s in text]
print(arr)