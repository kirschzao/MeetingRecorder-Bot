from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



def redirectGoogleMeet(driver, meet_link):
  driver.get(meet_link)
  print("✅ Redirecionamento para o Meet")