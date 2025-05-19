# import os
# import time
# import shlex
# import subprocess
# import tempfile

# # Importações necessárias para o Selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# # Variáveis globais para armazenar os processos criados neste módulo
# _xvfb_process = None
# _pulseaudio_process = None


# def initialize_environment(display=":99", resolution="1280x720", color_depth=24):
#     """
#     Inicializa o ambiente headless:
#       - Inicia o Xvfb para criar um display virtual.
#       - Inicia o PulseAudio com um null sink para capturar áudio.
#     """
#     global _xvfb_process, _pulseaudio_process

#     # Inicia o Xvfb (tela virtual)
#     xvfb_cmd = f"Xvfb {display} -screen 0 {resolution}x{color_depth} -ac"
#     _xvfb_process = subprocess.Popen(shlex.split(xvfb_cmd),
#                                      stdout=subprocess.PIPE,
#                                      stderr=subprocess.PIPE)
#     # Define a variável de ambiente DISPLAY para os aplicativos gráficos
#     os.environ["DISPLAY"] = display
#     time.sleep(2)  # Aguarda o Xvfb inicializar

#     # Inicia o PulseAudio em modo start
#     pulseaudio_cmd = "pulseaudio --start --exit-idle-time=-1"
#     _pulseaudio_process = subprocess.Popen(shlex.split(pulseaudio_cmd),
#                                            stdout=subprocess.PIPE,
#                                            stderr=subprocess.PIPE)
#     time.sleep(2)  # Aguarda o PulseAudio iniciar

#     # Carrega o módulo null sink para criar um dispositivo de áudio virtual
#     subprocess.call(
#         "pactl load-module module-null-sink sink_name=DummySink", shell=True)
#     subprocess.call("pactl set-default-sink DummySink", shell=True)
#     time.sleep(2)
#     print("✅ Ambiente (Xvfb e PulseAudio) inicializado com sucesso!")


# def stop_environment(driver=None):

#     global _xvfb_process, _pulseaudio_process
#     if _pulseaudio_process:
#         _pulseaudio_process.terminate()
#         _pulseaudio_process.wait()
#         print("PulseAudio finalizado.")
#     if _xvfb_process:
#         _xvfb_process.terminate()
#         _xvfb_process.wait()
#         print("Xvfb finalizado.")

#     if driver:
#         try:
#             driver.quit()
#             print("ChromeDriver finalizado.")
#         except Exception as e:
#             print("Erro ao finalizar o ChromeDriver:", e)