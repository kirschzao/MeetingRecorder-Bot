from app.bot.Bot import Bot
import time

class Pipeline:
  def __init__(self, meetLink: str, botName: str):
    self.meetBot = Bot(meetLink, botName)
  
  def run(self):
    
    try:
      #PASSO 1: Iniciar o ambiente


      #PASSO 2: Entrar na reunião
      self.meetBot.joinMeet()
      
      #PASSO 3: Iniciar a gravação

      
      #PASSO 4: Verifica se esta na reunião
      self.meetBot.stayOnMeet()

      #PASSO 5: Encerra Gravação


      #PASSO 6: Encerra o ambiente

    
    except Exception as e:
      return e
