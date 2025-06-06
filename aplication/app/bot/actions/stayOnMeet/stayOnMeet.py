from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from app.bot.actions.stayOnMeet.verifyMembers import verifyMembers
from app.bot.actions.stayOnMeet.removeBot import removeBot
import time

def stayOnMeet(driver):

    time.sleep(2)

    while True:
        # Verifica se foi expulso da reunião
        if (removeBot(driver)):
            break

        # Verifica a quantidade de participantes
        if (verifyMembers(driver)):
            break

    driver.quit()

