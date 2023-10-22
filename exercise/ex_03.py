# 輸入正整數N，判斷N是否為質數。
# 輸入正整數N，印出小於N的所有質數
n = int(input("輸入正整數 : "))
def check_prime_num(n:int):
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
    return is_prime

def print_all_prime_num(n:int):
    for i in range(n):
        if check_prime_num(i) == True:
            print(i, end=",")

if check_prime_num(n) == True:
    print(f"{n} 是質數")
else:
    print(f"{n} 不是質數")

print(f"印出所有小於 {n} 的質數：")
print_all_prime_num(n)