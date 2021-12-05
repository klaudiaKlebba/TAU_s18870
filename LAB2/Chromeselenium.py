from selenium import webdriver
import logging
import time
from selenium.common.exceptions import NoSuchElementException


logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
#
# #Zalando - Chrome
# logger.info('Przechodzę na stronę Zalando')
# driver.get('https://www.zalando.pl/')
#driver.maximize_window()
# time.sleep(3)
# pop = driver.find_element_by_id('uc-btn-accept-banner')
# pop.click()
# time.sleep(2)
# temp = driver.find_element_by_class_name('z-navicat-header_navToolItemLink')
# temp.click()
# time.sleep(2)
# temp = driver.find_element_by_id('login.email')
# temp.click()
# temp.send_keys('Halinkap@wp.pl')
# temp = driver.find_element_by_id('login.secret')
# temp.click()
# temp.send_keys('kotnaplocie')
# time.sleep(2)
# temp = driver.find_element_by_xpath('//button[@class="DJxzzA u9KIT8 uEg2FS U_OhzR ZkIJC- Vn-7c- '
#                                      'FCIprz heWLCX JIgPn9 LyRfpJ pxpHHp Md_Vex NN8L-8 GTG2H9 MfX1a0 '
#                                      'WCjo-q EKabf7 aX2-iv r9BRio mo6ZnF E6Km4r"]')
# temp.click()
# time.sleep(2)
# try:
#     zalndo_error = driver.find_element_by_xpath('//span[@class="u-6V88 ka2E9k uMhVZi FxZV-M _6yVObe pVrzNP"]')
#     print("Error appeared, test number 1 passed")
# except NoSuchElementException:
#     print("Error doesn't appear")
#
# driver.close()

#Test 2 - chrome - aolx.pl
logger.info('Rozpoczynam test na stronie olx.pl')

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

driver.get('https://www.olx.pl/')
driver.maximize_window()
time.sleep(3)
pop = driver.find_element_by_id('onetrust-accept-btn-handler')
pop.click()
time.sleep(2)
temp = driver.find_element_by_id('topLoginLink')
temp.click()
temp = driver.find_element_by_id('register_tab')
temp.click()
time.sleep(2)
temp = driver.find_element_by_id('userEmailRegister')
temp.click()
temp.send_keys('Halinkap@wp.pl')
time.sleep(2)
temp = driver.find_element_by_id('userPassRegister')
temp.click()
temp.send_keys('kotnaplocie12')
temp = driver.find_element_by_id('button_register')
temp.click()
time.sleep(2)
try:
    olx_error = driver.find_element_by_class_name('error')
    print("Error appeared, test number 1 passed")
except NoSuchElementException:
    print("Error doesn't appear")


driver.close()
