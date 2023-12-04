# 自行選定目標網頁進行爬取。例如：統一發票開獎。
import requests
from bs4 import BeautifulSoup

html=requests.get("https://invoice.etax.nat.gov.tw/")
bs=BeautifulSoup(html.text,"html.parser")
tables=bs.find_all("table")
print(tables)