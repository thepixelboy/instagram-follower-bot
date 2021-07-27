import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    username = self.driver.find_element_by_name("username")
    password = self.driver.find_element_by_name("password")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    time.sleep(2)
    password.send_keys(Keys.ENTER)


def find_followers(self):
    time.sleep(5)
    self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

    time.sleep(2)
    followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers.click()

    time.sleep(2)
    # modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    modal = self.driver.find_element_by_css_selector(".isgrP")
    for i in range(10):
        # In this case we're executing some Javascript, that's what the execute_script() method does.
        # The method can accept the script as well as a HTML element.
        # The modal in this case, becomes the arguments[0] in the script.
        # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
