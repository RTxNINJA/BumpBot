from dotenv import load_dotenv
from time import sleep
import requests
import os

load_dotenv()
_token = os.getenv('TOKEN')
_channelID = os.getenv('CHANNEL_ID')

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
            self.session = requests.post(f"https://discord.com/api/v9/channels/{self.channelID}/messages", data=self.data, headers=self.header)
            sleep(self.minute * 121)

bBot = Bot(authToken=_token, channelID=_channelID, message="/bump")
bBot.run()
