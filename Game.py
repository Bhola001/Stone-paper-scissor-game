'''
Stone = 1
Paper = 0
Scissors = -1
'''
def game():
    import random
    computer = random.choice([1,0,-1])

    Select = input("Enter your word:")
    L = Select.lower()
    Cap = L.capitalize()

    Dicyou = {"Stone":1, "Paper":0, "Scissors":-1}
    You = Dicyou[Cap]

    reversedDic = {1:"Stone", 0:"Paper", -1:"Scissors"}
    C = reversedDic[computer]

    print("Computer Choise:", C)

    print("Your choise:",Cap)

    if (computer==You):
        print("It's a Draw")

    else:
    # if(computer== 1 and You == 0):  computer-You =1
    #    print("You win")
    
    # elif(computer== 1 and You == -1):  computer-You =2
    #    print("Computer win")

    # elif(computer== 0 and You == 1):  computer-You =-1
    #   print("Computer is win")

    # elif(computer== 0 and You == -1):  computer-You 1
    #   print("You win")

    # elif(computer== -1 and You == 1):  computer-You =-2
    #   print("You win") 

    # elif(computer== -1 and You == 0):  computer-You =-1
    #   print("Computer win")

      if(computer-You == 1 or computer-You == -2):
        print("You win")

      elif(computer-You == -1 or computer-You == 2):
        print("Computer win")        

      else:
        print("Something is wrong")

    return game()

print(game()) # same as game()