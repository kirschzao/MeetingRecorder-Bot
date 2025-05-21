from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import os

def initializeChrome():
    try:
        opt = Options()
        opt.add_argument("--no-first-run")
        opt.add_argument("--disable-gpu")
        opt.add_argument("--disable-software-rasterizer")
        opt.add_argument("--disable-features=VizDisplayCompositor")
        opt.add_argument("--disable-dev-shm-usage")
        opt.add_argument("--disable-background-networking")
        opt.add_argument("--no-sandbox")
        opt.add_argument("--disable-blink-features=AutomationControlled")
        opt.add_argument("--start-maximized")
        opt.add_argument("--start-fullscreen")

        # Caminho para o arquivo .y4m com a imagem que simula a câmera
        #base_dir = os.path.dirname(os.path.abspath(__file__))
        #caminho_video_simulado = os.path.abspath(os.path.join(base_dir, "../../../assets/fake.y4m"))
        # Simula câmera e microfone automaticamente com arquivo de vídeo
        #opt.add_argument("--use-fake-device-for-media-stream")
        #opt.add_argument("--use-fake-ui-for-media-stream")
        #opt.add_argument(f"--use-file-for-fake-video-capture={caminho_video_simulado}")


        # Diretório de perfil temporário (simula "modo anônimo")
        temp_profile_dir = tempfile.mkdtemp()
        opt.add_argument(f"--user-data-dir={temp_profile_dir}")

        # Permissões automáticas para mídia
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 0,
            "profile.default_content_setting_values.media_stream_camera": 0,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1,
        })

        driver = webdriver.Chrome(options=opt)
        print("✅ Driver do Chrome inicializado com sucesso!")
        return driver

    except Exception as e:
        print("❌ Erro ao inicializar o Chrome:", e)
        return None

