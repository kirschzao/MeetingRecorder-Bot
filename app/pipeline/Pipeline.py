from app.bot.Bot import Bot
from app.recorder import Recorder
from app.recorder.Recorder import Recorder
from app.bot.actions.enviroment.initialize_environment import startDisplay
import time

class Pipeline:
  def __init__(self, meetLink: str, botName: str):
    self.meetBot = Bot(meetLink, botName)
    self.recorder = Recorder()
  
  def run(self):
    
    try:
      #PASSO 1: Iniciar o ambiente
      display = startDisplay()

      #PASSO 2: Entrar na reunião
      self.meetBot.joinMeet()
      
      #PASSO 3: Iniciar a gravação
      self.recorder.startRec()
      
      #PASSO 4: Verifica se esta na reunião
      self.meetBot.stayOnMeet()

      #PASSO 5: Encerra Gravação
      self.recorder.stopRec()

      #PASSO 6: Encerra o ambiente
      display.stop()
    
    except Exception as e:
      return e
