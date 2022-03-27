from dotenv import load_dotenv
from time import sleep
import requests
import os

channelID = '863515625712648192'

load_dotenv()
_token = os.getenv('TOKEN')

class Bot:
    def __init__(self, authToken, channelID, message):
        self.authToken = authToken
        self.channelID = channelID
        self.message = message

        self.header = {'authorization': self.authToken}
        self.data = {'content': self.message}

        self.second = 1
        self.minute = 60
        self.hour = 3600

    def run(self):
        while True:
            self.session = requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", data=self.data, headers=self.header)
            sleep(self.minute * 121)

bBot = Bot(authToken=_token, channelID='863515625712648192', message="/bump")
bBot.run()
