import os
import subprocess
import shlex
import sys

def gerar_video_y4m_da_foto(
    nome_foto="foto.jpeg",       # ajuste para “foto.jpeg” ou “foto.jpg” conforme o nome exato
    nome_saida="camera.y4m",
    duracao_segundos=10,
    largura=640,
    altura=480,
    fps=30
):
    """
    Gera um vídeo Y4M a partir de uma única imagem (nome_foto),
    repetindo-a em loop por duracao_segundos, para simular câmera fake.

    - nome_foto: arquivo JPEG/PNG na mesma pasta do script
    - nome_saida: nome do arquivo Y4M gerado
    - duracao_segundos: duração total do vídeo em segundos
    - largura, altura: resolução do vídeo (ex.: 640x480)
    - fps: quadros por segundo (ex.: 30)
    """

    # 1) Verifica se o arquivo existe
    if not os.path.isfile(nome_foto):
        print(f"✖️  '{nome_foto}' não encontrado na pasta atual ({os.getcwd()}).")
        sys.exit(1)

    # 2) Comando FFmpeg para criar vídeo Y4M a partir da imagem em loop
    cmd = (
        f"ffmpeg -y "
        f"-loop 1 -i {shlex.quote(nome_foto)} "
        f"-vf scale={largura}:{altura} "
        f"-r {fps} "
        f"-t {duracao_segundos} "
        f"-pix_fmt yuv420p "
        f"{shlex.quote(nome_saida)}"
    )

    # 3) Executa o FFmpeg e captura a saída para verificação de erro
    processo = subprocess.run(
        shlex.split(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if processo.returncode != 0:
        print("✖️  Falha ao gerar o arquivo Y4M. Mensagem de erro do FFmpeg:\n")
        print(processo.stderr.decode("utf-8", errors="ignore"))
        sys.exit(1)
    else:
        print(f"✔️  Vídeo '{nome_saida}' criado com sucesso.")

if __name__ == "__main__":
    # Ajuste aqui o nome do arquivo de foto se for 'foto.jpg' ou outra extensão:
    gerar_video_y4m_da_foto(
        nome_foto="foto.jpg",       # certifique-se de usar exatamente “foto.jpeg” ou “foto.jpg”
        nome_saida="camera.y4m",
        duracao_segundos=3,
        largura=1280,
        altura=720,
        fps=1
    )
