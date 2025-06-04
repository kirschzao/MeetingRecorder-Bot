from pyvirtualdisplay import Display
import os
import subprocess
import shlex
import time
import signal

def startDisplay():
    cmd = "Xvfb :99 -screen 0 1280x720x24 -nolisten tcp"
    proc = subprocess.Popen(
        shlex.split(cmd),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    # Aguarda meio segundo para o Xvfb subir
    time.sleep(0.5)
    # Exporta DISPLAY=:99 para o ambiente do script
    os.environ["DISPLAY"] = ":99"
    print("🖥️  Xvfb em :99 iniciado (manualmente)")
    return proc
