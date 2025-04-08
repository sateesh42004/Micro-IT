import random
lis=["rock","paper","scissors"]
def computers_choice():
  c_choice=random.choice(lis)
  return c_choice
def game():
  p_score=0
  c_score=0
  while(1):
    print("1.rock","2.paper","scissors","enter your choice: ",sep="\n")
    p_choice=input()
    if p_choice not in lis[::]:
      print("your choice is wrong, chose correct choice: ")
      continue
    com_choice=computers_choice()
    if (p_choice=="rock" and com_choice=="scissors") or (p_choice=="scissors" and com_choice=="paper") or (p_choice=="paper" and com_choice=="rock"):
      p_score=p_score+1
      print("yours choice: ",p_choice+" and ")
      print("computers choice: ",com_choice)
      print("wow you won the game "+ "your score is: ",p_score)
      c=int(input("enter 1 to continue or 0 to stop game: "))
      if c==0:
        print("thanks for playing "+ "your score is: ",p_score)
        print("computer score is: ",c_score)
        break
    else:
      c_score=c_score+1
      print("yours choice: ",p_choice+ " and ")
      print("computers choice: ",com_choice)
      print("yours bad luck computer own the match and computer score is : ",c_score)
      c=int(input("enter 1 to continue or 0 to stop game: "))
      if c==0:
        print("thanks for playing "+ "your score is: ",p_score)
        print("computer score is: ",c_score)
        break

  if p_score>c_score:
    print("you won the match with score: ",(p_score-c_score))
  else:
    print("you loose the game with score: ",(c_score-p_score))
game()
