import requests

def changeStatus():
    url = ""
    token= ""

    headers = {
    "Authorization": token,
    "Content-Type": "application/json"
    }

    data = {
        "ID_BOT": "ss",
        "ID_USER": "",
        "Status": "",
    }

    response = requests.post(url, json=data)


def sendVideoToAWS():
    AWS_USER_PATH = ""
    url= ""

    data = {
        "ID_BOT": "",
        "ID_USER": "",
        "Status": ""
    }

    response = requests.post(url, json=data)






#ID_BOT = ""
#ID_USER = ""
#MEET_LINK = "https://meet.google.com/ugs-vzys-mua"
#BOT_NAME = "BeasyBot"
#MEET_NAME = "Produto"
#STATUS = "BUILDING"
#AWS_ADDRES= ""