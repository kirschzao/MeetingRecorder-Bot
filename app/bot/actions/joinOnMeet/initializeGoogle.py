from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

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
        opt.add_argument("--start-maximized")

        temp_profile_dir = tempfile.mkdtemp()
        opt.add_argument(f"--user-data-dir={temp_profile_dir}")
        
        # Configura preferências experimentais
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1,
        })

        driver = webdriver.Chrome(options=opt)
        driver.set_window_position(0, 0)
        driver.set_window_size(1920, 1080)

        print("✅ Driver do Chrome inicializado com sucesso!")
        return driver

    except Exception as e:
        print("❌ Erro ao inicializar o Chrome:", e)
        return None
