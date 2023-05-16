import os 
import time
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from modules.get_element import get_element

def send_snapchat(driver, user, message, meme=False):

    def select_user(user):
        users_name_elem = get_element(driver, "FiLwP", "CLASS_NAME")

        for e in users_name_elem:
            print(e.text)
            if e.text == user:
                if users_name_elem[-1].text == user:
                    return
                ActionChains(driver)\
                    .click(e)\
                    .perform()
                return
        raise Exception(f"THE USER: {user} WASN'T FOUD, CRITICAL")
        
    def send_message(message):
        text_box = get_element(driver, "/html/body/main/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div")
        ActionChains(driver)\
            .click(text_box)\
            .perform()
        
        ActionChains(driver)\
            .send_keys(message)\
            .send_keys(Keys.ENTER)\
            .perform()
        
        if meme:
            meme_path = os.getcwd()+"/src/images/memes/"
            meme_image = meme_path + str(random.choice(os.listdir(meme_path)))

            input_box = get_element(driver, "/html/body/main/div[1]/div[2]/div/div/div/div[2]/div[2]/div/button/input")
            input_box.send_keys(meme_image)
            time.sleep(1)
            ActionChains(driver).send_keys(Keys.ENTER).perform()

    select_user(user)

    if isinstance(message, list):
        for e in message:
            send_message(e)
    else:
        send_message(message)

    # return to main page:
    button = get_element(driver, "/html/body/main/div[1]/div[2]/div/div/div/div[1]/div[1]/button")
    button.click()

    return