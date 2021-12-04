from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pyautogui

from get_stock_names import *

options = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

browser.get('https://in.investing.com/')
browser.maximize_window()

try:
  last_stock_name = extracted_stock_name[-1]
  last_stock_index = stock_names.index(last_stock_name)
except:
  last_stock_index = 0
print(stock_names)
print(last_stock_index)

time.sleep(5)
links_list = []
search_input = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[2]/input')
for company_name in stock_names[last_stock_index+1:]:
  name = company_name.split()
  try:
    time.sleep(5)
    search_input.click()
    search_input.send_keys(company_name)
    filter_button = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[3]/div/div[2]/ul/li[1]/button/div/div/div/span/span[2]')
    filter_button2 = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[3]/div/div[2]/ul/li[2]/button/div')
    if filter_button:
      pyautogui.hotkey('ctrl', 'a')
      joined_string = ' '.join(name[:2])
      search_input.send_keys(joined_string)
      time.sleep(3)
      first_list_element = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[3]/div/div[2]/ul/li[1]/div/div[1]/section/div[1]/div/div/a[1]')
      first_list_element.click()
      time.sleep(5)
    elif filter_button2:
      pyautogui.hotkey('ctrl', 'a')
      joined_string = ' '.join(name[:1])
      search_input.send_keys(joined_string)
      time.sleep(3)
      first_list_element = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[3]/div/div[2]/ul/li[1]/div/div[1]/section/div[1]/div/div/a[1]')
      first_list_element.click()
      time.sleep(5)
    else:
      time.sleep(3)
      first_list_element = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[3]/div/div[2]/ul/li[1]/div/div[1]/section/div[1]/div/div/a[1]')
      first_list_element.click()
      time.sleep(5)
  except:
    time.sleep(5)
    search_input.click()
    pyautogui.hotkey('ctrl', 'a')
    joined_string = ' '.join(name[:2])
    search_input.send_keys(joined_string)
    time.sleep(3)
    first_list_element = browser.find_element_by_xpath('//*[@id="js-main-container"]/header/section/div[2]/div/div[3]/div/div[2]/ul/li[1]/div/div[1]/section/div[1]/div/div/a[1]')
    first_list_element.click()
    time.sleep(5)

  stock_url_dict = {'Stock Name': company_name, 'Stock Link': browser.current_url}
  stock_urls = stock_urls.append(stock_url_dict, ignore_index=True)
  stock_urls.to_csv('files/stock_links.csv')
  print(stock_urls)




