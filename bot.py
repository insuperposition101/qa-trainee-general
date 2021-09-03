import slack 
import json

f = open ("example.json")
data = json.load(f)

client = slack.WebClient(token = data ['bot_token'])

channels = data ['channels']

for message in channels:

    client.chat_postMessage(
        channel = message['channel'],
        text = message['text']
    )


# client.chat_postMessage(
#     channel="#test1", 
#     text="Hello world!"
# )
# client.chat_postMessage(
#     channel="#test2", 
#     text="Hello world?"
# )
# client.chat_postMessage(
#     channel="#test3", 
#     text="Hello world :)"
# )