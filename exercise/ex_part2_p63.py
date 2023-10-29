# 開啟文字檔，讀取所有資料並在每行的前面加上編號並輸出，最後計算文章共有幾個字。
with open("ex_part2_p63.txt","r", encoding="utf-8") as f:
    word_num = 0
    i = 0
    for line in f:
        print(f"{i}{line}", end="")
        word_num += len(line)
        i += 1
    print(f"\n總共 {word_num} 字")