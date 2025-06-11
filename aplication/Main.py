from app.pipeline.Pipeline import Pipeline, Status
import os
from dotenv import load_dotenv

if __name__ == "__main__":
  load_dotenv()

  idBot = os.getenv("ID_BOT")
  idUser = os.getenv("ID_USER")
  meetlink = os.getenv("MEET_LINK")
  meetName = os.getenv("MEET_NAME")
  botName = os.getenv("BOT_NAME")
  awsUserPath = os.getenv("AWS_USER_PATH")
  apiKey = os.getenv("API_KEY")
  
  print("idBot:", idBot)
  print("idUser:", idUser)
  print("link:", meetlink)
  print("meetName:", meetName)
  print("botName:", botName)
  print("awsUserPath:", awsUserPath)
  print("apiKey:", apiKey)
  
  pipeline = Pipeline(meetlink, botName, meetName).run()

