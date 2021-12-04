from selenium import webdriver
import logging
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#Test 3 -Firefox - OLX
# driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
# logger.info('Rozpoczynam test na stronie olx.pl')
#
#
# driver.get('https://www.olx.pl/')
# driver.maximize_window()
# time.sleep(3)
# pop = driver.find_element_by_id('onetrust-accept-btn-handler')
# pop.click()
# time.sleep(2)
# temp = driver.find_element_by_id('topLoginLink')
# temp.click()
# temp = driver.find_element_by_id('userEmail')
# temp.click()
# temp.send_keys('Halinkap@wp.pl')
# temp = driver.find_element_by_id('userPass')
# temp.click()
# temp.send_keys('kotnaplocie')
# temp = driver.find_element_by_id('se_userLogin')
# temp.click()
# time.sleep(2)
# try:
#     olx_error = driver.find_element_by_class_name('errorboxContainer')
#     print("Error appeared, test number 1 passed")
# except NoSuchElementException:
#     print("Error doesn't appear")
#
# driver.close()

#Test 3 -Firefox - pyszne.pl
driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
logger.info('Rozpoczynam test na stronie olx.pl')


driver.get('https://www.olx.pl/')
driver.maximize_window()
time.sleep(2)
pop = driver.find_element_by_id('onetrust-accept-btn-handler')
pop.click()
olx_apps = driver.find_element_by_id('footerLinkMobileApps')
time.sleep(3)
olx_apps.click()
try:
    olx_app_icons = driver.find_element_by_class_name("app-icons")
    print("App icons exist, test number 3 passed")
except NoSuchElementException:
    print("App icons don't exist")


driver.close()

