import os
import time
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def get_driver():
    print("Starting client...")
    base_url = "https://web.snapchat.com/"
    dirname = os.path.dirname(__file__)
    unique_id = str(int(time.time())) + f"_{os.getpid()}"  # Add process ID for uniqueness
    driver_user_path = os.path.join(dirname, "../driver_user", unique_id)

    # Clean up old driver_user directories
    parent_dir = os.path.join(dirname, "../driver_user")
    try:
        for old_dir in os.listdir(parent_dir):
            old_dir_path = os.path.join(parent_dir, old_dir)
            if os.path.isdir(old_dir_path) and old_dir != unique_id:
                print(f"Cleaning up old directory: {old_dir_path}")
                shutil.rmtree(old_dir_path, ignore_errors=True)
    except Exception as e:
        print(f"Failed to clean up old directories: {e}")

    try:
        os.makedirs(driver_user_path, exist_ok=True)
        os.chmod(driver_user_path, 0o777)
    except Exception as e:
        print(f"Failed to create user data directory {driver_user_path}: {e}")
        return None

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument(f'--user-data-dir={driver_user_path}')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install(), log_path="/app/chromedriver.log")
    try:
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Failed to start Chrome: {e}")
        return None

    driver.set_page_load_timeout(30)

    try:
        driver.get(base_url)
        print(f"Successfully loaded {base_url}")
    except Exception as e:
        print(f"Failed to load {base_url}: {e}")
        driver.quit()
        return None

    return driver