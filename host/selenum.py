from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from TripTnT.settings import MEDIA_ROOT
from bs4 import BeautifulSoup

import cssutils
import urllib

class UrlScrapper:

	def __init__(self, *args, **kwargs):

		
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1920x1080")
		
		chrome_driver = os.getcwd() +"/chromedriver"
	

		self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
		self.soup = None
		# driver.find_element_by_xpath('.//div[@class="_1n57hdr7"]/button[@class="_n5wk6ic"]').click()
		


	def scrape_property(self, url):

		
		self.driver.get(url)
		self.soup = BeautifulSoup(self.driver.page_source,'lxml')
		
		title = self.soup.find('h1',class_='_1xu9tpch').text
		attributes = self.soup.find_all('span', class_='_fgdupie')
		house_rules = self.soup.find('div', id='house-rules').find_all('div',class_='_ncwphzu')
		price_string = self.soup.find('span', class_='_doc79r').text
		price = price_string[1:]
		address = self.soup.find('div', class_='_ncwphzu').text
		cancellations_search= self.soup.find_all('div', class_='_1n57hdr7')
		amenities = self.soup.find('div', class_='_2h22gn').find_all('div',class_='_ncwphzu')
		cancellations = cancellations_search[3].text

		highlights = self.soup.find_all('span', class_='_12i0h32r')
        
		highlight1 = highlights[4].text
		highlight2 = highlights[5].text

		highlight1_text = attributes[4].text
		highlight2_text = attributes[5].text


		# availability = self.soup.find('div', class_='_fgdupie').text	
		guest = attributes[0].text
		bedroom = attributes[1].text
		beds = attributes[2].text
		bath = attributes[3].text
		amenities = [amenity.text for amenity in amenities]
		house_rule = [rules.text for rules in house_rules]

      	#to get cover image from css
		div_style = self.soup.find('div',class_='_30cuyx5')['style']
		style = cssutils.parseStyle(div_style)
		back_url = style['background-image']
		back_url = back_url.replace('url(','').replace(')','')
		image = title.split()
		image_name = ("-").join(image)+'.jpg'
		#provide media url to image
		image_url = '/media/'+image_name
		#save image in media_cdn
		urllib.request.urlretrieve(back_url, '../media_cdn/'+image_name)

		scraper_data = {
		'title':title,
		'guest': guest,
		'bedroom': bedroom,
		'beds': beds, 
		'bath': bath,
		'house_rules': house_rule, 
		'price':price,
		'image_url':image_url,
		'address':address,
		'cancellations':cancellations,
		'image_name':image_name,
		'platform_link':url,
		'amenities': amenities,
		'highlight1': highlight1,
		'highlight2': highlight2,
		'highlight1_text': highlight1_text,
		'highlight2_text': highlight2_text,
		}

		self.driver.close()
		return scraper_data
	             




