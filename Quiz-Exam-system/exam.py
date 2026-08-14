import os

print("I am using:", os.path.abspath("questions.txt"))


def start_quiz():
  score=0
  with open("questions.txt","r") as file:
    data=file.readlines()
    for x in data:
      line=x.strip().split("|")
      print()
      print(line[0])
      for opt in range(1,5):
        print(f"option {opt}:{line[opt]}")
      while True:
        try:
          val=int(input("Enter your option:"))
          if val>4 or val<1:
            raise ValueError("enter option (1-4)")
        except ValueError as e:
          print(e)
        else:
          break
      if str(val)==line[5]:
        score+=1
      else:
        print("Wrong answer")
  print(f"Your score is {score}/{len(data)}")
          
      
  
def add_question(ques,op1,op2,op3,op4,ans):
  append="\n"+ques+"|"+op1+"|"+op2+"|"+op3+"|"+op4+"|"+str(ans)
  with open("questions.txt","a") as file:
    file.write(append)
    
    
def view_questions():
  with open("questions.txt","r") as file:
    data=file.readlines()
    for x in data:
      line=x.split("|")[0]
      print(line)
      print()
            
  
def search_question(ques):
  with open("questions.txt","r") as file:
    data=file.readlines()
    for line in data:
      x=line.strip().split("|")
      for val in x:
        if ques.upper() in val.upper():
          print(x[0])
          print()
      