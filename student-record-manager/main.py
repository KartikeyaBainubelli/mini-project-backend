from student import(
  add_students,
  view_students,
  search_students,
  delete_students,
  update_students
) 
while True:
  print("\n-----student-record-manager-----")
  print()
  print("1.Add Students")
  print("2.View Students")
  print("3.Search Students")
  print("4.Delete Students")
  print("5.Update Students")

  
  print()
  try:
    choice=int(input("Enter your choice:"))
    
    match choice:
      case 1: 
        name=input("Enter name:")
        student_id=int(input("enter id:"))
        add_students(name,student_id)
        
        
        
      case 2:
        view_students()
        
        
        
      case 3:
        try:
          name=input("students name:")
          search_students(name)
        except ValueError as e:
          print(e)
  
      case 4:
        student_id=input("enter id of the student you want to delete:")
        delete_students(student_id)
        
        
        
      case 5:
        s=int(input("enter student id"))
        n=input("enter new name")
        m=int(input("enter new marks"))
        update_students(s,n,m)
      
      case _:
        print("Invalid choice")
    
    
  except ValueError:
    print("Enter enter a number")