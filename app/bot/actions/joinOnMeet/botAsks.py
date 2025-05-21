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



def askToJoin(driver):
    # Ask to Join meet
    time.sleep(2)
    driver.implicitly_wait(2000)
    driver.find_element(
        By.CSS_SELECTOR, 'button[jscontroller="O626Fe"][data-promo-anchor-id="w5gBed"]').click()
    print("⏱️ Pedindo Permissao para entrar (la ele KKKKKK)")

    entrou = False

    while not entrou:
        print("⏱️ Verificando se já entrou na reunião...")
        if checkIfJoined(driver):
            entrou = True
        else:
            print("Ainda não é o momento. Verificando novamente...")
            time.sleep(0.5)


def checkIfJoined(driver):
    try:
        # Verifica se o elemento está presente na página
        driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Você entrou na reunião"]')
        print("✅ Entrou na reunião!")
        return True
    except NoSuchElementException:
        # O elemento não foi encontrado, o que significa que ainda não entrou na reunião
        return False
    except TimeoutException:
        # Ocorreu um timeout ao esperar pelo elemento
        print("⏱️ Timeout ao verificar se entrou na reunião.")
        return False