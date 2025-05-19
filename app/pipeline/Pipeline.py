from app.bot.Bot import Bot
import time

class Pipeline:
  def __init__(self, meetLink: str, botName: str):
    self.meetBot = Bot(meetLink, botName)
  
  def run(self):
    # initialize_environment(display=":99", resolution="1280x720", color_depth=24)
    
    #PASSO 1: Entrar na reunião
    driver = self.meetBot.joinMet()

    #PASSO 2: Começar a gravar
