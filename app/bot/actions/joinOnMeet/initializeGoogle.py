import os
import time
import shlex
import subprocess
import tempfile

# Importações necessárias para o Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def initializeChrome():
    try:
        # Configurar opções do Chrome
      opt = Options()
      opt.add_argument("--incognito") 
      opt.add_argument("--no-first-run")
      opt.add_argument("--no-sandbox")
      opt.add_argument("--disable-software-rasterizer")
      opt.add_argument("--disable-extensions")
      opt.add_argument("--disable-application-cache")
      opt.add_argument("--disable-setuid-sandbox")
      opt.add_argument("--disable-dev-shm-usage")
      opt.add_argument("--disable-background-networking")
      opt.add_argument("--window-size=720")
      opt.add_argument("--disable-gpu")
      opt.add_argument('--disable-blink-features=AutomationControlled')
      opt.add_argument('--start-maximized')
      opt.add_argument('--window-position=0,0')

        # Cria um diretório temporário exclusivo para o perfil e adiciona o argumento
      temp_profile_dir = tempfile.mkdtemp()
      opt.add_argument(f"--user-data-dir={temp_profile_dir}")

        # Configura preferências experimentais
      opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1,
        })

        # Inicializa o driver do Chrome com o gerenciador de drivers
      driver = webdriver.Chrome(options=opt)
      driver.set_window_rect(0, 0, 1080, 720)
      print("✅ Driver do Chrome inicializado com sucesso!")
      return driver

    except Exception as e:
      print("Erro ao inicializar o Chrome:", e)
      return None