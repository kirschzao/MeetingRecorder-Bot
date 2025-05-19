from app.bot.Bot import Bot
from app.bot.actions.enviroment import initialize_environment 


class Pipeline:
  def __init__(self, meetLink: str, botName: str):
    self.meetBot = Bot(meetLink, botName)
  
  def run(self):
    initialize_environment(display=":99", resolution="1280x720", color_depth=24)
    #entrar na reunião:
    driver = self.meetBot.joinMet()


    #sair da reunião:
