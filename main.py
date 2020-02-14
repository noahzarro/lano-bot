import telegram
import json

with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)


bot = telegram.Bot(token=token_dict["token"])
