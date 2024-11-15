import player
import computer


def judge():
     if(player(1) and computer(2) or player(2) and computer(3) or player(3) and computer(1)):
        print(F"あなたの手:{player}")
        print(F"相手の手:{computer}")
        return("あなたの勝ちです！")
     elif(player(1) and computer(1) or player(2) and computer(2) or player(3) and computer(3)):
        print(F"あなたの手:{player}")
        print(F"相手の手:{computer}")
        return("あいこです、もう一度！")
     else:
        print(F"あなたの手:{player}")
        print(F"相手の手:{computer}")
        return("コンピュータの勝ちです。")
       
            
    


