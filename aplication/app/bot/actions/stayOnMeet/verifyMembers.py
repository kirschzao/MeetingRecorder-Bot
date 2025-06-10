import time
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By



def verifyMembers(driver):
    try:
        participantes = driver.find_elements(
                        By.CSS_SELECTOR, '[jscontroller="h8UR3d"]'
                    )
        print(f"👥 Participantes: {len(participantes)}", flush=True)

        if len(participantes) <= 1:
            print("✅ Só ficou 1 participante!", flush=True)
            exitMeet(driver)
            return True
        
        return False
    except:
        return True


def exitMeet(driver):
    # Espera o botão de sair da reunião aparecer
    exit_button = driver.find_element(By.CSS_SELECTOR, '[jsname="CQylAd"]')
    exit_button.click()
    print("🚪 Saiu da reunião.", flush=True)
    





