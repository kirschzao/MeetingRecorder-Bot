from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .meetConfigs import initializeChrome
from .redirectMeet import redirectGoogleMeet
from .botAsks import botName, askToJoin
import time


def joinOnMeet(meetLink: str, name: str):
  driver = initializeChrome()
  print("✅ Driver do Chrome inicializado com sucesso!")
  
  redirectGoogleMeet(driver, meetLink)
  print("✅ Redirecionamento para o Meet concluído!")   
  
  botName(driver, name) 
  print("✅ Nome inserido com sucesso!")
  
  if askToJoin(driver):
    print("✅ Entrou na reunião!")
  else:
    raise Exception("❌ Sua solicitação para entrar na chamada foi recusada.")
  
  
  return driver

  