from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import tempfile
import os

def initializeChrome():
    try:
        opt = Options()
        opt.add_argument("--incognito")
        opt.add_argument("--no-first-run")
        opt.add_argument("--disable-gpu")
        opt.add_argument("--disable-software-rasterizer")
        opt.add_argument("--disable-features=VizDisplayCompositor")
        opt.add_argument("--disable-dev-shm-usage")
        opt.add_argument("--disable-background-networking")
        opt.add_argument("--no-sandbox")
        opt.add_argument("--disable-blink-features=AutomationControlled")
        opt.add_argument("--window-size=1280,720")  # Tamanho da janela do Chrome
        opt.add_argument("--start-fullscreen")
        opt.add_argument("--start-maximized")
        opt.add_argument("--disable-infobars")


        # Simula câmera e microfone automaticamente com arquivo de vídeo
        opt.add_argument("--use-fake-device-for-media-stream")
        opt.add_argument("--use-fake-ui-for-media-stream")
        caminho_video_simulado = os.path.join(os.path.dirname(__file__), "..", "..","..", "assets", "camera.y4m")
        caminho_video_simulado = os.path.abspath(caminho_video_simulado)
        if not os.path.exists(caminho_video_simulado):
            raise FileNotFoundError(f"Arquivo de vídeo simulado não encontrado: {caminho_video_simulado}")
        opt.add_argument(f"--use-file-for-fake-video-capture={caminho_video_simulado}")


        # Diretório de perfil temporário (simula "modo anônimo")
        temp_profile_dir = tempfile.mkdtemp()
        opt.add_argument(f"--user-data-dir={temp_profile_dir}")

        # Permissões automáticas para mídia
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1,
            "profile.default_content_setting_values.popups": 2,
        })
        opt.add_experimental_option("useAutomationExtension", False)
        opt.add_experimental_option("excludeSwitches", ["enable-automation"])


        driver = webdriver.Chrome(options=opt)
        largura = driver.execute_script("return window.innerWidth")
        altura = driver.execute_script("return window.innerHeight")


        print(f"Resolução da janela do Chrome: {largura}x{altura}")
        return driver

    except Exception as e:
        print("❌ Erro ao inicializar o Chrome:", e)
        return None

