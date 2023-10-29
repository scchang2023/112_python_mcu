# 利用鍵盤輸入兩個整數，透過第三個變數，將兩個整數值交換並輸出。
# 挑戰：不透過第三個變數，完成兩數交換。

a = int(input("輸入第一個整數 a :"))
b = int(input("輸入第二個整數 b :"))

# 透過第三個變數
# temp = a
# a = b
# b = temp

# 不透過第三個變數
a, b = b, a
print(f"兩個數值交換後 a={a}, b={b}")

# import pyinputplus as pyip
# x = pyip.inputInt("輸入第一個整數 x :")
# y = pyip.inputInt("輸入第二個整數 y :")
# print(f"x={x}, y={y}")