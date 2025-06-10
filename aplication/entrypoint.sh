#!/usr/bin/env bash
set -e


pulseaudio --start --daemonize=true --system=false --disallow-exit || true
# 1) Inicia Xvfb em :99 (display virtual para x11grab)
Xvfb :99 -screen 0 1280x720x24 -nolisten tcp &
# 2) Define DISPLAY para que o FFmpeg use esse display
export DISPLAY=":99"

# 3) Executa o script Python principal
exec python Main.py
