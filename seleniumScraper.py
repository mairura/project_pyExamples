# NOTE!!!!
# Needs an update

from selenium import webdriver

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.booking.com/cheap/city/ke/nairobi.html')
print(driver.page_source)
