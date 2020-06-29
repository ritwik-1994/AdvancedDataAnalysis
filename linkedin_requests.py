from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import time

#Logging intoo Linkedin
def login():

	driver.find_element_by_class_name('main__sign-in-link').click()
	username_input = driver.find_element_by_name('session_key')
	time.sleep(1)
	username_input.send_keys("Enter-Username")
	password_input = driver.find_element_by_name('session_password')
	time.sleep(1)
	password_input.send_keys("Enter-Password")
	driver.find_element_by_xpath('//button[text()="Sign in"]').click()
#Redirecting to My Network
def goto_network():
	try:
		driver.find_element_by_id("mynetwork-tab-icon").click()
	except:
		print("[+] Some Error Occured \n Directly Opening netoworks Tab")
		body = driver.find_element_by_tag_name("body")
		body.send_keys(Keys.CONTROL +'t')
		driver.get(nurl)
#Using PyAutoGUI to click repeatedly
def get_details():
	for i in range(0,30):
		time.sleep(5)		
		pag.click(483,975)
		time.sleep(5)
		print("["+str(i)+"] Connection request sent ")
		driver.refresh()
	print("Done")

driver = webdriver.Chrome('/home/shipsy/chromedriver')
url = "http://linkedin.com"
nurl = "http://linkedin.com/mynetwork"
driver.get(nurl)
login()
goto_network()
get_details()

