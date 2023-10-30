# 輸入兩個正整數，求兩數之和。
# 程式中，若輸入非數值資料，以 try⋯except 捕捉發生的錯誤。
try:
    n1 = int(input("輸入正整數 n1 ："))
    n2 = int(input("輸入正整數 n2 ："))
    print(f"兩數之和：{n1+n2}")
except Exception as e:
    print(f"輸入錯誤：{e}")