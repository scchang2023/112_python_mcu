# 自行選定目標網頁進行爬取。例如：統一發票開獎。
import requests

html=requests.get("https://invoice.etax.nat.gov.tw/")
print(html.text)