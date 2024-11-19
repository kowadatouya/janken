import player
import computer
import janken_judge

def janken_main():
    janken_hand = ['グー', 'チョキ', 'パー']
    count = 0
   
    playercount = 0
    computercount = 0
    
    while count < 3:
        playerhand = player.pon()
        computerhand = computer.pon()
        janken_judge.judge(playerhand, computerhand)
        count += 1
 
        
    result = janken_judge.judge(playerhand, computerhand)
    if result:
        playercount += 1
    print(F"あなた:{playercount}勝")
    print(F"コンピュータ:{3 - playercount}勝")
    if(playercount >= 2):
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です。")
        
janken_main()
    
            
            