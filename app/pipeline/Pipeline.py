from app.bot.Bot import Bot
import time

class Pipeline:
  def __init__(self, meetLink: str, botName: str):
    self.meetBot = Bot(meetLink, botName)
  
  def run(self):
    # initialize_environment(display=":99", resolution="1280x720", color_depth=24)
    
    try:
      #PASSO 1: Iniciar o ambiente

      #PASSO 2: Entrar na reunião
      self.meetBot.joinMeet()
      
      #PASSO 3: Verifica se esta na reunião
      self.meetBot.stayMeet()

      #PASSO 4: Encerra processos
    
    except Exception as e:
      return e
