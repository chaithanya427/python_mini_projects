import random
initial, end = 1, 10
playing_flag= True
guesses= 0
def Generate_Number(initial,end):
    Generate_Num=random.randint(initial,end)
    return Generate_Num
Generate_Num=Generate_Number(initial,end)


while playing_flag : 
    guessed_Num = input(f"Try Guessing a number between {initial} to {end}: ")
    if guessed_Num.isdigit() :
        guessed_Num=int(guessed_Num)
        if guessed_Num >= initial and guessed_Num <= end :
            if guessed_Num < Generate_Num:
                guesses+=1
                print("Guessed lesser number")
            elif guessed_Num > Generate_Num:
                guesses+=1
                print("Guessed greater number")  
            elif Generate_Num == guessed_Num : 
                guesses+=1
                print(f"You won after {guesses} guesses")
                play_again= input("Wanna play again Y/N")
                if play_again.upper()=='Y': 
                    Generate_Num,guesses=Generate_Number(initial,end),0

                else:
                    playing_flag=False
                    print("Thank You for playing!")
            
        else:
            print("You have guessed out of range number.. Try Again !")
    else:
        print("Only INT Accepted")





