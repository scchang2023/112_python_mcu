# 利用鍵盤輸入兩個整數，透過第三個變數，將兩個整數值交換並輸出。
# 挑戰：不透過第三個變數，完成兩數交換。
try:
    x = int(input("輸入第一個整數 x :"))
    y = int(input("輸入第二個整數 y :"))
    # temp = x
    # x = y
    # y = temp
    print(f"x={x}, y={y}")
    x, y = y, x
    print(f"兩個數值交換後 x={x}, y={y}")    
except:
    print("應用程式錯誤")

# import pyinputplus as pyip
# x = pyip.inputInt("輸入第一個整數 x :")
# y = pyip.inputInt("輸入第二個整數 y :")
# print(f"x={x}, y={y}")