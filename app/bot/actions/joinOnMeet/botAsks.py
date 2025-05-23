import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def botName(driver, text_to_insert):
  try:
  # Aguarda até que o elemento input esteja visivel (timeout de 30 segundos)
    input_field = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')))
  # Limpa o campo (opcional) e insere o texto
    input_field.clear()
    input_field.send_keys(text_to_insert)
    
    return driver
  except Exception as e:
    print("Erro ao inserir a string no input:", e)



def askToJoin(driver, timeout_seconds=60):
    """
    Clica em ‘Pedir para entrar’ e aguarda até:
      – detectar que entrou (True)
      – detectar mensagem de erro/recusa (False)
      – ou estourar o timeout (False)
    """
    # Clica no botão de pedir permissão
    print("⏳ Aguardando o botão de pedir permissão...")
    driver.implicitly_wait(10)
    try:
        driver.find_element(
            By.CSS_SELECTOR,
            'button[jscontroller="O626Fe"][data-promo-anchor-id="w5gBed"]'
        ).click()
    except NoSuchElementException:
        print("❌ Botão de pedir permissão não encontrado.")
        return False

    start = time.time()
    while True:
        # 1) Checou se entrou?
        if checkIfJoined(driver):
            return True

        # 2) Checou se apareceu mensagem de recusa/erro?
        if checkIfRejected(driver):
            return False

        # 3) Timeout
        if time.time() - start > timeout_seconds:
            print(f"⏱️ Timeout de {timeout_seconds}s ao tentar entrar.")
            return False

        time.sleep(0.5)


def checkIfJoined(driver):
    try:
        join_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[jscontroller="h8UR3d"]'))
        )
        print("✅ Dentro da Chamada")
        return True
    except:
        return False
    

def checkIfRejected(driver):
    try:
        join_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.cMgZMe'))
        )
        print("❌ Solicitação para entrar na chamada recusada")
        return True
    except:
        return False



