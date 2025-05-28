from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def get_element(driver, input, search_type="XPATH", timeout=20):
    try:
        print(f"Searching for element: {input} using {search_type}")
        if search_type == "XPATH":
            return WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, str(input)))
            )
        if search_type == "CLASS_NAME":
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, str(input)))
            )
    except TimeoutException:
        print(f"Timeout waiting for element {input} after {timeout} seconds")
        return None
    except WebDriverException as e:
        print(f"WebDriver error while searching for {input}: {e}")
        return None