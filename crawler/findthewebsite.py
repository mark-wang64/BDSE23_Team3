from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import re  
options = webdriver.ChromeOptions()
# prefs:設定不會跳出網頁通知
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome(chrome_options = options)
# 城市爬蟲的網址
browser.get("https://www.tripadvisor.com/Hotels-g186220-Bristol_England-Hotels.html") 
bs = BeautifulSoup(browser.page_source, 'html.parser')
time.sleep(2)
ActionChains(browser).move_by_offset(1, 1).click().perform()
# 創建各飯店網頁的列表
html_list = []
# 抓取總頁數
pages = round(int(re.sub("\D", "",bs.find('span',{'class':'eMoHQ'}).text))/30)+1


htm=bs.find_all('a',{'class':'property_title prominent'})
for i in htm:
    html_list.append(i.get('href'))
try:
    # 下一頁爬蟲開始
    for i in range(pages-1):
        print(i)
        time.sleep(7)
        browser.find_element_by_link_text('Next').click()  
        bs = BeautifulSoup(browser.page_source, 'html.parser')
        htm=bs.find_all('a',{'class':'property_title prominent'})
        for b in htm:
            html_list.append(b.get('href'))
except IndexError:
    print('finish')
finally:
# 檔案存檔
    df=pd.DataFrame(columns=[
            '網址'])
    df['網址'] = pd.Series(html_list)
    df1=df.drop_duplicates()
    df1.to_csv('Bristol.csv',encoding = 'utf-8_sig',index = False) # 儲存的檔案名稱和路徑
    




