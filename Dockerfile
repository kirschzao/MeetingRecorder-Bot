FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    pulseaudio \
    xvfb \
    x11vnc \
    tini \
    wget \
    gnupg2 \
    ca-certificates \
    unzip \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends google-chrome-stable \
  && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix


RUN useradd -m appuser \
    && mkdir -p /home/appuser/.config/pulse \
    && chown -R appuser:appuser /home/appuser/.config

USER appuser

WORKDIR /home/appuser/aplication

COPY --chown=appuser:appuser aplication/ /home/appuser/aplication/

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
