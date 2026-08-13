def add_students(name,student_id):
  
  with open("students.txt","r") as file:
    data=file.read().split()
    arr=[int(string.split(",")[0]) for string in data]
    last=arr[len(arr)-1]+1
  with open("students.txt","a") as file:
    newval=(str(last)+","+name+","+str(student_id))
    file.write("\n"+newval)
  




def view_students():
    with open("students.txt","r") as file:
      print("Student data:")
      print(file.read())
      
      
      
      
def search_students(name):
  with open("students.txt","r") as file:
          data=file.readlines()
          found=False
          for line in data:
              if name.upper() in line.upper():
                print("data:" ,end=" ")
                print(line)
                found=True
                break
          if not found:
            raise ValueError(f"Student {name} not found")
 
 
 
              
def delete_students(student_id):
  with open("students.txt","r") as file:
    data =file.readlines()
  new_data=[]
  for s in data:
    x=s.split(",")[0]
    if x!=str(student_id):
      new_data.append(s)
  with open("students.txt","w") as file:
    file.writelines(new_data)
      
      
      
def update_students(student_id,student_name,student_marks):
  with open("students.txt","r") as file:
    data=file.readlines()
  for x in range(len(data)):
    if str(student_id)==data[x].split(",")[0]:
      data[x]=str(student_id)+","+student_name+","+str(student_marks)
  with open("students.txt","w") as file:
    file.writelines(data)