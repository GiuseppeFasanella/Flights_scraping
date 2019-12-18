from flights_utils import *
from selenium import webdriver ##To load content dynamically
#You need selenium to parse a website that is "not complete": i.e. with info generated on the fly with JS
#https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

### These things should became arguments
start = get_place_id("Bari")
destination = get_place_id("Milano")
date='2020-01-01'
currency='CHF'


## Se il server Selenium non è lanciato, lancialo
## xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.13.0.jar
url = create_url(start, destination, date, currency)
driver = webdriver.Chrome()
driver.get(url)
#print(driver.find_element_by_css_selector('.gws-flights-results__cheapest-price').text)
#print(driver.find_element_by_css_selector('.gws-flights-form__menu-button').text) #This gives Solo Andata
#print(driver.find_element_by_css_selector('.gws-flights__results').text) #This does not work
driver.quit()
