from app.pipeline.Pipeline import Pipeline
import os
from dotenv import load_dotenv

if __name__ == "__main__":
  load_dotenv()
  link = os.getenv("LINK")
  botName = os.getenv("BOT_NAME")
  meetName = os.getenv("MEET_NAME")
  
  print(link, botName, meetName)
  pipeline = Pipeline(link, botName, meetName).run()
  print("✅✅✅✅✅ Pipeline executado com sucesso!")
