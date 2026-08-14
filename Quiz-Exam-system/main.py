from exam import (
  start_quiz,
  add_question,
  view_questions,
  search_question
)
while True:
  print("-----PYTHON QUIZ-----")
  print()
  print("1. Start Quiz")
  print("2. Add Question")
  print("3. View Questions")
  print("4. Search Question")
  print("5. Exit")
  
  
  
  try:
    choice=int(input("Enter your choice:"))
    match choice:
      
      case 1:
        start_quiz()
        
      case 2:
        ques=input("Enter question:")
        op1=input("Enter option 1:")
        op2=input("Enter option 2:")
        op3=input("Enter option 3:")
        op4=input("Enter option 4:")
        ans=int(input("Enter correct option:"))
        add_question(ques,op1,op2,op3,op4,ans)
      
      case 3:
        view_questions()  
      
      case 4:
        ques=input("enter a keyword to find the question:")
        search_question(ques)
        print()
        
      case 5:
        break
      
      case _:
        print("Invalid choice")
    
  except ValueError:
    print("Enter a number")
    