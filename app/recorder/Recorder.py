import subprocess
import signal
import os

class Recorder:
    def __init__(self):
        self.proc = None

    def startRec(self):
        output_path = "Nome da Reuniao.mp4"
        fps = 15
        largura, altura = 1280, 720

        # Garante que DISPLAY esteja definido
        if "DISPLAY" not in os.environ:
            os.environ["DISPLAY"] = ":99"

        cmd = [
            "ffmpeg",
            "-y",
            "-draw_mouse", "0",  # Desabilita o cursor do mouse
            # Buffer para evitar dropped frames
            "-rtbufsize", "1500M",

            # Captura de vídeo via X11
            "-f", "x11grab",
            "-video_size", f"{largura}x{altura}",
            "-framerate", str(fps),
            "-i", ":99",

            # Captura de áudio via PulseAudio
            "-f", "pulse",
            "-i", "default",

            # Codec de vídeo e configurações de alta qualidade
            "-codec:v", "libx264",
            "-preset", "ultrafast",
            "-crf", "15",
            "-profile:v", "high",
            "-level", "4.2",
            "-tune", "stillimage",
            "-pix_fmt", "yuv420p",
            "-threads", "0",

            # Codec de áudio
            "-c:a", "aac",

            output_path
        ]

        self.proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            env=os.environ.copy()
        )
        print("Gravação iniciada (vídeo + áudio).")

    def stopRec(self):
        if not self.proc:
            return
        proc = self.proc
        if proc.poll() is None:
            try:
                proc.stdin.write(b"q")
                proc.stdin.flush()
                proc.wait()
            except Exception:
                proc.send_signal(signal.SIGINT)
                proc.wait()
            print("Gravação finalizada.")
