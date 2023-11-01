a=1
b=100
ans=38

while(True):
    guess=int(input(f"請輸入數字{a}~{b}:"))
    if(guess<=a or guess>=b):
        continue
    if(guess==ans):
        print("答對了!")
        break
    if(guess>ans):
        b=guess
    if(guess<ans):
        a=guess

