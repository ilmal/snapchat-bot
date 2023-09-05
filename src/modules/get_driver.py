import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def get_driver():

    print("Strating client...")

    base_url = "https://web.snapchat.com/"

    dirname = os.path.dirname(__file__)
    driver_user_path = dirname.replace("modules", "driver_user")

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    #options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    options.add_argument(str('--user-data-dir=' + driver_user_path)) # use a custom profile


    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.get(base_url)

    return driver