from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



def redirectGoogleMeet(driver, meet_link):
  driver.get(meet_link)
  driver.implicitly_wait(60)
  print("✅ Redirecionamento para o Link do Google Meet concluído!")