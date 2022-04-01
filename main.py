from telethon import TelegramClient, sync, events
import json


api_id: int
api_hash: str
chat_name: str


with open("keys.json", "r", encoding="utf8") as keys_file:
    data = json.load(keys_file)
    api_id = int(data[0]["api_id"])
    api_hash = data[0]["api_hash"]
    chat_name = data[0]["chat_name"]


client = TelegramClient("Test session", api_id, api_hash)
client.start()
print("Client has been connected.")

@client.on(events.NewMessage(chats=(chat_name)))
async def handle_message(event):
    message = event.message.to_dict()
    print(message["message"])

client.run_until_disconnected()
