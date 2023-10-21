# 終極密碼。
# 玩法：其中一人做莊，給定一個數字範圍，再從中選出一個自然數，此數字稱為「密碼」，
# 不能讓其他參與遊戲者得知。而遊戲參與者輪流猜測數字。每猜一個數，
# 莊家就要告知遊戲者該數字是大於或小於密碼，直至密碼被猜中。(維基百科)
import random
min = 1
max = 100
target = random.randint(min, max)

while True:
    keyin = int(input(f"猜密碼，範圍 {min}~{max} :"))
    if keyin == target:
        print("猜中了")
        break
    elif keyin > target:
        print("再小一點")
    elif keyin < target:
        print("再大一點")