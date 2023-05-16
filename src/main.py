import os
import time

from modules.snapchat.snapchat_send import send_snapchat
from modules.snapchat.story_pusher import post_story
from modules.get_driver import get_driver
from modules.snapchat.snapchat_listener import snap_listener

from bot_explanations.answers import answers
from bot_explanations.random_explanations import random_explanations


def main(driver):
    # listen for new messages
    chat_user, chat_message = snap_listener(driver)

    if chat_message == "beep" or chat_message == "Beep":
        print("He said beep!")
        send_snapchat(driver, chat_user, "boop")
        return

    if chat_message:
        print("he said something!", chat_message)
        #send_snapchat(driver, chat_user, "Ah, I see, did you mean this?", True)
        send_snapchat(driver, chat_user, [answers(chat_message), random_explanations()])


def init():
    # define driver and open page
    driver = get_driver()
    #post_story()
    counter = 0
    while True:
        counter += 1
        main(driver)
        time.sleep(.5)

        if counter >= 4320:
            counter = 0
            post_story()



if __name__ == "__main__":
    init()