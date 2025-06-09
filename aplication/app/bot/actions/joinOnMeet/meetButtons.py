from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def muteMic(driver):
    try:
        micButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[jsname="hw0c9"]')))
        micButton.click()
        print("✅ Mic mutado com sucesso")
    except (TimeoutException, NoSuchElementException):
        print("❌ Não foi possível desativar o microfone")

        
def cleanPopupGotIt(driver):
    try:
        popUpButton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[jsname="EszDEe"]'))).click()
        print("✅ Popup 'Got it' encontrado e ignorado")
    except (TimeoutException, NoSuchElementException):
        print("✅ Popup 'Got it' não encontrado ou já fechado")