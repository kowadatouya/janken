import player
import computer
import janken_judge

def janken_main():
    count = 0
    playercount = 0
    computercount = 0
    playerhand = player.pon()
    computerhand = computer.pon()
    
    while count < 3:
        if(playerhand == 1 and computerhand == 2 or playerhand == 2 and computerhand == 3 or playerhand == 3 and computerhand == 1):
            print(F"あなたの手:{player}")
            print(F"相手の手:{computer}")
            print(janken_judge.judge())
            count += 1
            playercount += 1
        elif(playerhand == 1 and computerhand == 1 or playerhand == 2 and computerhand == 2 or playerhand == 3 and computerhand == 3):
            print(F"あなたの手:{player}")
            print(F"相手の手:{computer}")
            print(janken_judge.judge())
        else:
            print(F"あなたの手:{player}")
            print(F"相手の手:{computer}")
            print(janken_judge.judge())
            count += 1
            computercount += 1
            
            
    print(F"あなた:{playercount}勝")
    print(F"あなた:{computercount}勝")
    if(playercount >= 2):
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です。")
        
janken_main()
    
            
            