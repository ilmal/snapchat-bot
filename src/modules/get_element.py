from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_element(driver, input, search_type="XPATH"):
    try:
        DELAY = 10
        if search_type == "XPATH":
            return WebDriverWait(driver, DELAY).until(EC.presence_of_element_located(
                (By.XPATH, str(input))))
        if search_type == "CLASS_NAME":
            return WebDriverWait(driver, DELAY).until(EC.visibility_of_all_elements_located(
                (By.CLASS_NAME, str(input))))
    except TimeoutException:
        print("Loading took too much time!")
        driver.quit()