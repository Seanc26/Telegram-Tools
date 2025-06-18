#this script downloads all media (videos and images) from the selected channel, DM or group even if saving is disabled


import os
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

# Replace these with your actual API credentials
api_id = [API ID]  # int, no quotes
api_hash = '[API HASH]'  # string, keep quotes

# The username, ID or invite link of your private channel
channel = [123456]

# Folder to save downloaded media
download_folder = 'downloads'
os.makedirs(download_folder, exist_ok=True)

with TelegramClient('session_name', api_id, api_hash) as client:
    print(f'Connected to Telegram. Fetching messages from {channel}...')
    
    for message in client.iter_messages(channel):
        if message.photo:
            print(f'Downloading photo from message {message.id}')
            client.download_media(message.photo, file=download_folder)
        elif message.document:
            # Check if document is video or image by mime type
            if message.file and message.file.mime_type:
                if 'video' in message.file.mime_type or 'image' in message.file.mime_type:
                    print(f'Downloading document from message {message.id} (mime: {message.file.mime_type})')
                    client.download_media(message.document, file=download_folder)

print('Download completed.')
