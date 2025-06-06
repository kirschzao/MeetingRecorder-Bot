import time
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def removeBot(driver):
    try:
        # Verifica se o bot foi expulso da reunião
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[jsname="r4nke"].roSPhc'))
        )
        print("❌ Bot saiu da reunião!", flush=True)
        return True
        
    except (TimeoutException, WebDriverException):
        print("✅ Bot ainda está na reunião!", flush=True)
        return False