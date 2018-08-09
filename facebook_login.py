from selenium import webdriver

username = 'username@gmail.com'
password = 'p@ssword'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/shivang/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()