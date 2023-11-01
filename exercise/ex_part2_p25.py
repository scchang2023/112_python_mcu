# 先輸入一個整數N，再以迴圈方式輸入N個數字，並將這些數字存入串列中。
import pyinputplus as pyip
# list1 = []
# n1 = pyip.inputInt("輸入一整數：",min=0)   
# i = 0
# while i < n1:
#     n2 = pyip.inputInt(f"輸入第 {i+1} 個數字：")   
#     list1.append(n2)
#     i += 1
# print(f"輸入的串列：{list1}")

# 輸入一個整數N，將N項的費氏數列存到串列中。
# 所謂費波那契數列，是指在一串數字中，每一項是前兩項的和。
# 數學上的定義為：第 0 項 = 0、第 1 項 = 1、第 n 項 = 第 n-1 項 + 第 n-2 項。
# 從上面的數學定義，我們可以簡單列出數列的0 到 10 項為：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55。
n1 = pyip.inputInt("輸入一整數：", min=0)    
list1 = []
for i in range(n1):
    if i < 2:
        list1.append(i)
    else:
        list1.append(list1[-1]+list1[-2])
print(f"費氏數列：{list1}")