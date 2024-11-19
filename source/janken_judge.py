import player
import computer

def judge(playerhand, computerhand):
      playercount = 0
      computercount = 0
      janken_hand = ['グー', 'チョキ', 'パー']
      if(playerhand == 1 and computerhand == 2 or playerhand == 2 and computerhand == 3 or playerhand == 3 and computerhand == 1):
         print(F"あなたの手:{janken_hand[playerhand - 1]}")
         print(F"相手の手:{janken_hand[computerhand - 1]}")
         print("あなたの勝ちです！")
         playercount += 1
         return True
      elif(playerhand == 1 and computerhand == 1 or playerhand == 2 and computerhand == 2 or playerhand == 3 and computerhand == 3):
         print(F"あなたの手:{janken_hand[playerhand - 1]}")
         print(F"相手の手:{janken_hand[computerhand - 1]}")
         print("あいこです、もう一度！")
         playerhand = player.pon()
         computerhand = computer.pon()
         judge(playerhand, computerhand)
      else:
         print(F"あなたの手:{janken_hand[playerhand - 1]}")
         print(F"相手の手:{janken_hand[computerhand - 1]}")
         print("コンピュータの勝ちです。")
         computercount += 1
         return False
