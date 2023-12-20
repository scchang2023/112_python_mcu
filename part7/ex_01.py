from selenium import webdriver
import time

driver=webdriver.Chrome() 
driver.get("https://www.google.com.tw")
time.sleep(5)
driver.get("https://www.pchome.com.tw")
time.sleep(5)
driver.get("https://data.gov.tw/")
time.sleep(5)
driver.close()