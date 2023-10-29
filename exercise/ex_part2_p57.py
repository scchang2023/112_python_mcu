# 猜拳。
# 1剪刀、2石頭、3布，與電腦猜拳，並統計輸贏的次數。
import random as r

def get_winner(player:int, computer:int):
    # 0 剪刀、1 石頭、2 布
    # 0 平手, 1 player 贏, 2 computer 贏 
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

option_list = ["剪刀", "石頭", "布"]
winner_list = ["平手", "玩家", "電腦"]

while True:
    player_input_str = input("請輸入 [0]剪刀 [1]石頭 [2]布 : ")
    if player_input_str.isdigit() == False:
        print("輸入錯誤")
        continue
    player_input = int(player_input_str)
    if player_input > 2 or player_input <0:
        print("輸入超出範圍")
        continue
    computer_input = r.randint(0, 2)
    print(f"玩家出：{option_list[player_input]}")
    print(f"電腦出：{option_list[computer_input]}")
    winner = get_winner(player_input, computer_input)
    print(f"贏家是：{winner_list[winner]}")
    again_str = input("繼續玩? y/n : ")
    if  again_str != "y":
        break