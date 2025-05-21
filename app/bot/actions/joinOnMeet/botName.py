import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def botName(driver, text_to_insert):
  try:
  # Aguarda até que o elemento input esteja visível (timeout de 30 segundos)
    input_field = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')))
  # Limpa o campo (opcional) e insere o texto
    input_field.clear()
    input_field.send_keys(text_to_insert)
    print("✅ String inserida com sucesso!")
    
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

    while True:
        # Verifica se a condição de entrada é verdadeira
        if checkIfJoined(driver) == True:
            print("✅ Condição atendida! Iniciando gravação...")
            return True
            # Sai do loop após iniciar a gravação
        else:
            print("Ainda não é o momento. Verificando novamente...")

        # Aguarda um pouco antes da próxima verificação para evitar sobrecarga
        time.sleep(1)


def checkIfJoined(driver):
    try:
        # Wait for the join button to appear
        join_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[jscontroller="h8UR3d"]'))
        )
        print("✅ Dentro da Chamada")
        return True
    except Exception as e:
        print("Erro ao entrar na chamada")