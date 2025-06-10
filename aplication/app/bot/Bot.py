from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from app.bot.actions.joinOnMeet.joinMeet import joinOnMeet
from app.bot.actions.stayOnMeet.stayOnMeet import stayOnMeet
import time

class Bot:
  def __init__(self, meetLink: str, botName: str):
    self.meetLink = meetLink
    self.bot_name = botName
    self.driver = None
    
  def joinMeet(self):
    driver = joinOnMeet(self.meetLink, self.bot_name)
    self.driver = driver

  def stayOnMeet(self):
    stayOnMeet(self.driver)

  def close(self):
    self.driver.quit()

