# 利用鍵盤輸入兩個整數，透過第三個變數，將兩個整數值交換並輸出。
# 挑戰：不透過第三個變數，完成兩數交換。
import pyinputplus as pyip
a = pyip.inputInt("a=")
b = pyip.inputInt("b=")

# 透過第三個變數
# temp = a
# a = b
# b = temp

# 不透過第三個變數
a, b = b, a
print(f"a={a}, b={b}")