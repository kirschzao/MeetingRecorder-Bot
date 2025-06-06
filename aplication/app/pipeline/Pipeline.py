from app.bot.Bot import Bot
from app.recorder import Recorder
from app.recorder.Recorder import Recorder
from app.bot.actions.enviroment.initialize_environment import startDisplay
from enum import Enum
import time

class Pipeline:
  def __init__(self, meetLink: str, botName: str, meetName: str):
    self.meetName = meetName
    self.meetBot = Bot(meetLink, botName)
    self.recorder = Recorder()
    self.status = Status.BUILDING
  
  def run(self):
    
    try:
      #PASSO 1: Iniciar o ambiente
      display = startDisplay()

      #PASSO 2: Entrar na reunião
      self.status = Status.ASKING
      self.meetBot.joinMeet()
      
      #PASSO 3: Iniciar a gravação
      self.status = Status.RECORDING
      self.recorder.startRec(self.meetName)
      
      #PASSO 4: Verifica se esta na reunião
      self.meetBot.stayOnMeet()

      #PASSO 5: Encerra Gravação
      self.recorder.stopRec()
      self.status = Status.PROCESSING

      #PASSO 6: Encerra o ambiente
      display.stop()
    
    except Exception as e:
      self.status = Status.ERROR
      return e


class Status(Enum):
  BUILDING = 1
  ASKING = 2
  RECORDING = 3
  PROCESSING = 4
  ERROR = 5