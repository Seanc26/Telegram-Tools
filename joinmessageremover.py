#This script removes all exisiting join and leave messages from a group

from telethon.sync import TelegramClient
from telethon.tl.types import MessageActionChatJoinedByLink, MessageActionChatAddUser

# Replace these with your credentials
api_id = [API ID]  # your API ID
api_hash = '[API HASH]'  # your API hash
group = 'https://t.me/mygroup'  # or use group ID or exact name

with TelegramClient('session_name', api_id, api_hash) as client:
    for message in client.iter_messages(group):
        if message.action and isinstance(message.action, (
            MessageActionChatJoinedByLink,
            MessageActionChatAddUser,
        )):
            print(f"Deleting join message: {message.id}")
            client.delete_messages(group, message.id)
