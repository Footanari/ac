gmail = ""
password = ""
schedule = {
    "Mon": ["", ""],
    "Tue": ["", "", ""],
    "Wed": ["", ""],
    "Thu": ["", "", ""],
    "Fri": ["", ""],
    "Sat": [""],
    "Sun": [""]
}

from time import ctime, sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

path = r'.\chromedriver.exe'#download and put the path to chromedriver.exe here
driver = webdriver.Chrome(path)

def login():
    textbox = driver.find_element_by_name("identifier")
    textbox.send_keys(gmail)
    textbox.send_keys(Keys.RETURN)
    while True:
        try:
            textbox = driver.find_element_by_name("password")
            textbox.send_keys(password)
            textbox.send_keys(Keys.RETURN)
            break
        except:
            pass
def joinMeet():
    driver.switch_to.window(driver.window_handles[1])
    while(True):
        if driver.title[:4]=="Meet":
            sleep(3)
            ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            sleep(3)
            for a in range(5):
                #Tab goes brrrrrrrrrr
                ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            break
        else:
            sleep(60)
            driver.refresh()
    driver.switch_to.window(driver.window_handles[0])

while True:
    time = ctime()
    for clas in schedule.get(time[:3]):
        if time[11:16] == clas[:5]:
            driver.switch_to.window(driver.window_handles[0])
            driver.get("https://classroom.google.com/u/0/c/" + clas[5:])
            try:
                login()
            except:
                pass
            while True:
                try:
                    link = driver.find_element_by_partial_link_text("https://meet.google.com/lookup/")
                    link.click()
                    break
                except:
                    pass
            joinMeet()
    sleep(60)
