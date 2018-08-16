import requests
from bs4 import BeautifulSoup

def url_scrapper(listing_url):

   headers = {
   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0)',
   }
   
   try:
      source = requests.get(listing_url, headers = headers, timeout=10)
      soup = BeautifulSoup(source.content,'lxml')
      
      title = soup.find('span', class_='_12ei9u44').text
      attributes = soup.find_all('span', class_='_fgdupie')
      house_rules = soup.find('div', id='house-rules').find_all('div',class_='_ncwphzu')
      price = soup.find('span', class_='_doc79r')
      address = soup.find('div', class_='_ncwphzu').text
      guest = attributes[0].text
      bedroom = attributes[1].text
      beds = attributes[2].text
      bath = attributes[3].text
      house_rule = [rules.text for rules in house_rules]
      scraper_data = {
      'title':title,
      'guest': guest,
      'bedroom': bedroom,
      'beds': beds, 
      'bath': bath,
      'house_rules': house_rule, 
      'price':price,
      'address':address,
      'price_per_night':price
      }

      return scraper_data
   
   except requests.exceptions.Timeout:

      soup = None
      return None    
