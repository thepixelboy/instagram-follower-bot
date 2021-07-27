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
