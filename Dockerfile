# Usa a imagem oficial do Python 3.10 slim
FROM python:3.10-slim

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_ROOT_USER_ACTION=ignore

# Instala pacotes de sistema necessários
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    pulseaudio \
    xvfb \
    wget \
    gnupg2 \
    ca-certificates \
    unzip \
    x11vnc \
    && rm -rf /var/lib/apt/lists/*

# Instala o Tini (init process) para gerenciar processos zumbis
RUN apt-get update && apt-get install -y --no-install-recommends tini && rm -rf /var/lib/apt/lists/*

# Cria o usuário appuser (NÃO-ROOT)
RUN useradd -m appuser

# Atualiza o pip
RUN pip install --upgrade pip

# Instala o Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y --no-install-recommends google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Instala o ChromeDriver compatível com o Google Chrome
RUN CHROMEDRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && rm /tmp/chromedriver.zip && \
    chmod +x /usr/local/bin/chromedriver

# Define o diretório de trabalho (usando caminho absoluto)
WORKDIR /bot

# Copia o arquivo de requisitos
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . .

# Copia o script de entrypoint e altera suas permissões (executado como root)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Como root, antes de trocar para o usuário appuser:
USER root
RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

# Ajusta a propriedade do diretório de trabalho para o usuário appuser
RUN chown -R appuser:appuser /bot

# Define a variável de ambiente para o Xvfb
ENV DISPLAY=:99

# Para debug: desabilita o buffering do Python
ENV PYTHONUNBUFFERED=1

# Troca para o usuário não-root
USER appuser

# Configura o Tini como entrypoint para gerenciar processos zumbis,
# e depois executa o script de entrypoint que pode iniciar serviços e o app.
ENTRYPOINT ["/usr/bin/tini", "--", "/entrypoint.sh"]

# Comando padrão: inicia o aplicativo Python
CMD ["stdbuf", "-oL", "python", "-u", "server.py"]