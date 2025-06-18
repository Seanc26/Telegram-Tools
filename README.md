# telegram-tools 🛠️

**telegram-tools** is a collection of Python-based utilities built using the [Telethon](https://github.com/LonamiWebs/Telethon) framework. These tools are designed to give users enhanced control over their Telegram data by enabling chat inspection, media retrieval, and group cleanup operations.

## Features

- **Chat Inspector**: Retrieve the name, ID, and username of every direct message, group, and channel you have interacted with.
- **Media Extractor**: Download all images and videos from any specified chat, including cases where saving is disabled.
- **Service Message Remover**: Delete all historical "user joined" or "user left" system messages from any group you administer.

## Requirements

- Python 3.8 or higher
- Telethon (install via `pip install telethon`)

## Obtaining Telegram API Credentials

To use these tools, you need Telegram API credentials:

1. Visit [https://my.telegram.org](https://my.telegram.org)
2. Log in with your Telegram phone number.
3. Click on **API Development Tools**.
4. Complete the form (e.g., App title: `telegram-tools`, Short name: `tools`).
5. Copy your **API ID** and **API Hash** for use in the scripts.

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/Seanc26/telegram-tools.git
cd telegram-tools
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

5. Execute any script as needed:

```bash
python IDchecker.py
python mediadownloader.py
python joinmessageremover.py
```

## Important Notes

- You must be an admin with deletion rights to remove service messages from groups.
- For private groups or channels, ensure you are a member before attempting access.
- Keep your API credentials and session file secure.

## Script Descriptions

| Script                   | Functionality                                                                 |
|--------------------------|------------------------------------------------------------------------------|
| `IDchecker.py`          | Lists all DMs, groups, and channels along with their names, IDs, and usernames |
| `mediadownloader.py`      | Downloads all images and videos from a specified chat                         |
| `joinmessageremover.py` | Removes system messages (e.g., "user joined") from a group                  |


