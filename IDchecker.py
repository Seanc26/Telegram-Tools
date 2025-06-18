#This script outputs all of the private messages,groups and channels' name, ID and Username(if applicaple)

from telethon.sync import TelegramClient

api_id = [API ID]
api_hash = '[api hash]' #keep quotation marks

with TelegramClient('session_name', api_id, api_hash) as client:
    print("Listing all your chats and channels:\n")
    for dialog in client.iter_dialogs():
        print(f'Name: {dialog.name}')
        print(f'  ID: {dialog.id}')
        print(f'  Username: {dialog.entity.username}')
        print('------')
