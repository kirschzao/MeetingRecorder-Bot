from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .initializeGoogle import initializeChrome
from .redirectMeet import redirectGoogleMeet
from .botName import botName, askToJoin
import time

def joinMeet(meetLink: str, name: str):
  driver = initializeChrome()
  redirectGoogleMeet(driver, meetLink)   
  print("Calling botName function...")  # Debug: Check if this line is reached
  botName(driver, name) 
  askToJoin(driver)

  return driver

  
  
if __name__ == "__main__":
  joinMeet("https://meet.google.com/niw-jcwe-mgp?authuser=0", "teste")
  
  