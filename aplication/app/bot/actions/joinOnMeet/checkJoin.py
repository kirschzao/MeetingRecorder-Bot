from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def checkJoined(driver):
  try:
    join_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[jscontroller="h8UR3d"]')))
    print("✅ Dentro da Chamada")
    return True
  except (TimeoutException, NoSuchElementException):
    print("Erro ao entrar na chamada")