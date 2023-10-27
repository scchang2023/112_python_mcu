# 請使用格式化輸出或f-string的方法，將學生的姓名、數學成績、英語成績、以及總分統計輸出。
# 變數名稱：name="Alice"、Math=85、Eng=90，輸出格式如下。
"""
學生姓名：Alice
數學成績：85
英語成績：90
總分	：175
"""
name = "Alice"
Math = 85
Eng = 90
# 使用格式化
print("學生姓名：%s" % name)
print("數學成績：%d" % Math)
print("英語成績：%d" % Eng)
print("總分    ：%d" % (Math+Eng))
print()
# 使用 f-string
print(f"學生姓名：{name}")
print(f"數學成績：{Math}")
print(f"英語成績：{Eng}")
print(f"總分    ：{Math+Eng}")