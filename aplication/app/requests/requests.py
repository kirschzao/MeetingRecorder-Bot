import requests
from ..pipeline.Pipeline import Status
from dotenv import load_dotenv
import os
class Requests:
    def __init__(self, apiKey: str, botId: str, userId: str):
        self.headers = {"Authorization": "Beasy {apiKey}", "Content-Type": "application/json"}
        self.botId = botId
        self.userId = userId
        

    def changeStatus(self, status: Status):
        load_dotenv()
        url = os.getenv("API_URL", "http://localhost:5000/bot")
        data={
            "botId" :self.botId,
            "userId": self.userId,
            "status": status.value
        }
        response = requests.put(url, json=data, headers=self.headers)
        if response.status_code == 200:
            return True  # Retorna o conteúdo da resposta em formato JSON
        else:
            return f"Erro {response.status_code}: {response.text}"
        
    def sendVideoToAws():
        #if response.status_code == 200:
            return True  # Retorna o conteúdo da resposta em formato JSON
        #else:
           # return f"Erro {response.status_code}: {response.text}"

    