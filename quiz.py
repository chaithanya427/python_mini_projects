questions=["who is PM?","who is president?"]
options=[["A.Modi","B.patel","C.kovinth","D.billa"],["A.draupadi","B.lanka","C.ravana","D.Rama"]]
Answers= ["A.Modi","A.draupadi"]
Participant_guess = []
score=[]

import time
print("Quiz is about to start ...")
question_no=0
for e,q ,in enumerate(questions):
    print(f"Question {e+1}:{q}")
    for i in options[e]:
        print(i)
    # answer=input("enter your answer from the above options : ")
    while True:
        answer=input("enter your answer from the above options : ")
        if answer in options[e]:
            Participant_guess.append(answer)
            if answer==Answers[e]:
                score.append(1)
                print("Correct")
                break
            else:
                score.append(0)
                print("Incorrect")
                break
        else:
            print("Invalid selection, Please select from the above options")
        

scores=0
for i in score:
    scores=scores +i

print(f"Questions : {questions} And Player Answers are {Participant_guess}")
print(f" Your total score is {scores}")
  
 