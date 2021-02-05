gmail = ""
password = ""
schedule = {
    "Mon": ["", ""],
    "Tue": ["", "", "", ""],
    "Wed": ["", "", ""],
    "Thu": ["", "", "", ""],
    "Fri": ["", "", ""],
    "Sat": ["_"],
    "Sun": ["_"]
}
path = r'.\chromedriver.exe'#download and put the path to chromedriver.exe here

from time import ctime, sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

driver = webdriver.Chrome(path)

def login():
    while True:
        try:
            driver.get("https://accounts.google.com/signin/v2/identifier?hl=bg&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
            break
        except:
            print("connect earror")
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

login()
while True:
    time = ctime()
    for clas in schedule.get(time[:3]):
        if time[11:16] == clas[:5]:
            while True:
                try:
                    driver.get("https://meet.google.com/lookup/" + clas[5:] + "?authuser=1&hs=179")
                    break
                except:
                    print("connect earror")
            joinMeet()
    sleep(60)
