# 猜拳。
# 1剪刀、2石頭、3布，與電腦猜拳，並統計輸贏的次數。
import random as r
import pyinputplus as pyip

def get_winner(player:int, computer:int)->int:
    # 0:剪刀, 1:石頭, 2:布
    # 0:平手, 1:player贏, 2:computer贏
    winner = None
    if player == computer:
        winner = 0
    elif player == 0 and computer == 2:
        winner = 1
    elif player == 1 and computer == 0:
        winner = 1
    elif player == 2 and computer == 1:
        winner = 1
    else:
        winner = 2
    return winner

list_options = ["剪刀", "石頭", "布"]
list_winners = ["平手", "玩家", "電腦"]

while True:
    n1 = pyip.inputInt("請輸入 [0]剪刀 [1]石頭 [2]布 : ",min=0, max=2) 
    n2 = r.randint(0, 2)
    print(f"玩家出：{list_options[n1]}")
    print(f"電腦出：{list_options[n2]}")
    winner = get_winner(n1, n2)
    print(f"贏家是：{list_winners[winner]}")
    play_again = pyip.inputYesNo("繼續玩(y/n)？")
    print(play_again)
    if play_again == "no":
        break