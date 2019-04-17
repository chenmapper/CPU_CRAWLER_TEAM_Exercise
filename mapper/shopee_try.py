#1080415
#蝦皮試爬
import time
from selenium import webdriver  #從library中引入webdriver

chrome_path = "C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
driver = webdriver.Chrome(chrome_path)
url0='https://shopee.tw/'
url='https://shopee.tw/search?keyword=%E7%9A%AE%E5%8C%85'#皮包
i=1
driver.get(url)
dom=driver.page_source  #網頁原始碼
print(len(dom))
print(driver.current_url)#網頁URL
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='價格'])[1]/following::div[9]").click()
dom=driver.page_source  #網頁原始碼
print('第'+str(i)+'個商品網頁長度:',len(dom))
time.sleep(3)
print(driver.current_url)#網頁URL
driver.close()

