import player
import computer
import janken_judge

def janken_main():
    count = 0
    playercount = 0
    computercount = 0
    
    while count < 3:
        player()
        computer()
        if(player(1) and computer(2) or player(2) and computer(3) or player(3) and computer(1)):
            print(F"あなたの手:{player}")
            print(F"相手の手:{computer}")
            print(janken_judge.win)
            count += 1
            playercount += 1
        elif(player(1) and computer(1) or player(2) and computer(2) or player(3) and computer(3)):
            print(F"あなたの手:{player}")
            print(F"相手の手:{computer}")
            print(janken_judge.drow)
        else:
            print(F"あなたの手:{player}")
            print(F"相手の手:{computer}")
            print(janken_judge.lose)
            count += 1
            computercount += 1
            
            
    print(F"あなた:{playercount}勝")
    print(F"あなた:{computercount}勝")
    if(playercount >= 2):
        print("あなたの勝ちです！")
    else:
        print("コンピュータの勝ちです。")
    
            
            