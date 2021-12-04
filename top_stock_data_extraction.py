from get_stock_names import *

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {'User-Agent':str(ua.chrome)}

last_extracted_stock = stock_data.columns[-1]
print(last_extracted_stock)

if last_extracted_stock in extracted_stock_name:
 last_extracted_stock_index = extracted_stock_name.index(last_extracted_stock)
else:
 last_extracted_stock_index = 0

stocks_data_dict = {}

for name, link in zip(stock_urls['Stock Name'][last_extracted_stock_index:], stock_urls['Stock Link'][last_extracted_stock_index:]):
 stock_price_list = []
 print(name)
 url = f'{link}-historical-data?interval_sec=monthly'
 page = requests.get(url, headers=headers, timeout=5)

 soup = BeautifulSoup(page.content, "html.parser")

 dates = soup.find_all('td', attrs={'class': "col-rowDate"})
 prices = soup.find_all('td', attrs={'class': 'col-last_close'})

 for price in prices:
  price_amount = price.find('span', attrs={'class': 'text'})
  stock_price_list.append(price_amount.text)

 stock_data[name] = pd.Series(stock_price_list)
 stock_data.to_csv('files/stocks_data.csv')




url = f"{stock_urls['Stock Link'][1]}-historical-data?interval_sec=monthly"
page = requests.get(url, headers=headers, timeout=5)

soup = BeautifulSoup(page.content, "html.parser")

dates = soup.find_all('td', attrs={'class': "col-rowDate"})

stock_date_list = []

for date in dates:
 date_name = date.find('span', attrs={'class': 'text'})
 stock_date_list.append(date_name.text)

stock_data['Date'] = pd.Series(stock_date_list)
stock_data.to_csv('files/stocks_data.csv')