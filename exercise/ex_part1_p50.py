# 終極密碼。
# 玩法：其中一人做莊，給定一個數字範圍，再從中選出一個自然數，此數字稱為「密碼」，
# 不能讓其他參與遊戲者得知。而遊戲參與者輪流猜測數字。每猜一個數，
# 莊家就要告知遊戲者該數字是大於或小於密碼，直至密碼被猜中。(維基百科)
import random
import pyinputplus as pyip
min = 1
max = 100
pwd = random.randint(min, max)
# print(f"pwd = {pwd}")
while True:
    pwd_guess = pyip.inputInt(f"猜密碼，範圍 {min} ~ {max}：", min=min, max=max)    
    if pwd_guess == pwd:
        print("猜中了")
        break
    elif pwd_guess > pwd:
        max = pwd_guess-1
        print(f"再小一點")
    else:
        min = pwd_guess+1
        print(f"再大一點")