FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_ROOT_USER_ACTION=ignore

# 1) Instala pacotes de sistema (inclui ffmpeg, pulseaudio, xvfb, etc. + tini)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    pulseaudio \
    xvfb \
    wget \
    gnupg2 \
    ca-certificates \
    unzip \
    x11vnc \
    tini \
  && rm -rf /var/lib/apt/lists/*

# 2) Atualiza pip
RUN pip install --upgrade pip

# 3) Instala Google Chrome Stable
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends google-chrome-stable \
  && rm -rf /var/lib/apt/lists/*

# 4) Detecta o MAJOR do Chrome Stable instalado e baixa o Chromedriver compatível
RUN CHROME_MAJOR=$(google-chrome-stable --version | awk '{print $3}' | cut -d'.' -f1) \
  && CHROMEDRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR}") \
  && wget -q -O /tmp/chromedriver.zip \
       "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" \
  && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
  && rm /tmp/chromedriver.zip \
  && chmod +x /usr/local/bin/chromedriver

# 5) Cria usuário não-root e prepara pasta de config do PulseAudio
RUN useradd -m appuser \
  && mkdir -p /home/appuser/.config/pulse \
  && chown -R appuser:appuser /home/appuser/.config

USER appuser
WORKDIR /home/appuser/aplication

# 6) Copia requirements e instala dependências Python
COPY --chown=appuser:appuser requirements.txt /home/appuser/aplication/requirements.txt
RUN pip install --no-cache-dir -r /home/appuser/aplication/requirements.txt

# 7) Copia o restante do código
COPY --chown=appuser:appuser Main.py       /home/appuser/aplication/Main.py
COPY --chown=appuser:appuser .env          /home/appuser/aplication/.env
COPY --chown=appuser:appuser .gitignore    /home/appuser/aplication/.gitignore
COPY --chown=appuser:appuser app/          /home/appuser/aplication/app/

# 8) Copia entrypoint e dá permissão
COPY --chown=appuser:appuser entrypoint.sh /home/appuser/aplication/entrypoint.sh
RUN chmod +x /home/appuser/aplication/entrypoint.sh

# 9) Inicia PulseAudio + Xvfb e depois executa o Main.py
ENTRYPOINT ["/home/appuser/aplication/entrypoint.sh"]
