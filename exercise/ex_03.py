# 輸入正整數N，判斷N是否為質數。
# 輸入正整數N，印出小於N的所有質數
n = int(input("輸入正整數 N : "))
def check_prime_num(n:int)->bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_all_prime_num(n:int):
    for i in range(n):
        if check_prime_num(i) == True:
            print(i, end=",")

if check_prime_num(n) == True:
    print("質數")
else:
    print("不是質數")

print_all_prime_num(n)