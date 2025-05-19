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
  except Exception as e:
    print("Erro ao inserir a string no input:", e)