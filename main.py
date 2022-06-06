import time
from pynput.mouse import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

user = input("Enter your Gmail ID: ")
passwd = getpass.getpass()
classname = input("Enter the Name of Class you want to join (Google Classroom Name): ")

def cancel():
    mouse = Controller()
    mouse.position = (1309, 157)
    mouse.click(Button.left, 2)

def camera():
    mouse = Controller()
    mouse.position = (493, 659)
    mouse.click(Button.left, 1)

def join():
    mouse = Controller()
    mouse.position = (984, 517)
    mouse.click(Button.left, 1)

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting values.media_stream_mic" : 2}
options.add_experimental_option("prefs",prefs)
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,  # mic-->off
    "profile.default_content_setting_values.media_stream_camera": 2, #camera--> off
    "profile.default_content_setting_values.geolocation": 2,  # location--> off
    "profile.default_content_setting_values.notifications": 2 # notifications--> off
  })

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&continue=https%3A%2F%2Fclassroom.google.com%2F&ec=GAlAiQI&flowName=GlifWebSignIn&flowEntry=AddSession")

login = driver.find_element(By.NAME, "identifier")
login.send_keys( user + Keys.ENTER)
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
))
password.click()
password.send_keys( passwd + Keys.ENTER)
classroom = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="%s"]' % classname)
                                           )
)
classroom.click()
link= WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, ('https://meet.google.com/lookup/'))
                                           )
)
link.click()
cancelscreen = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'yDmH0d' )
                                           )
)
time.sleep(8)
cancel()
time.sleep(5)
camera()
join()
