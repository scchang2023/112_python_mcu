# 判斷13是否為質數
n=13
isPrime=True
for i in range(2,n):
    if(n%i==0):
        isPrime=False
        print(f"{n}不是質數")
        break
if(isPrime==True):
    print(f"{n}是質數")
    
# 印出小於19的所有質數  
# for n in range(2,20):
#     isPrime=True
#     for i in range(2,n):
#         if(n%i==0):
#             isPrime=False
#             #print(f"{n}不是質數")
#             break
#     if(isPrime==True):
#         print(f"{n}是質數")

