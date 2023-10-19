# 利用鍵盤輸入兩個整數，透過第三個變數，將兩個整數值交換並輸出。
# 挑戰：不透過第三個變數，完成兩數交換。
x = int(input("輸入第一個整數 x :"))
y = int(input("輸入第二個整數 y :"))
print(f"x={x}, y={y}")
# temp = x
# x = y
# y = temp
x, y = y, x
print(f"兩個數值交換後 x={x}, y={y}")

