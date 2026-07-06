import os

def safe_int(value, default=0):
    """Safely convert string to int with default fallback"""
    try:
        if not value:
            return default
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_bool(value, default=True):
    """Safely convert string to bool"""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes", "on")
    return default

class Config(object):
    # Required configurations with safe defaults
    API_ID = safe_int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "filestore_bot")
    DB_CHANNEL = safe_int(os.environ.get("DB_CHANNEL"))
    SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shortlink.com")
    SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
    BOT_OWNER = safe_int(os.environ.get("BOT_OWNER"))  # Will return 0 if 'kidzmc' or invalid
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    LOG_CHANNEL = safe_int(os.environ.get("LOG_CHANNEL"))
    
    # Handle banned users safely
    try:
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split() if x.strip().isdigit())
    except (ValueError, AttributeError):
        BANNED_USERS = set()
    
    # Boolean configs with safe parsing
    FORWARD_AS_COPY = safe_bool(os.environ.get("FORWARD_AS_COPY", "True"))
    BROADCAST_AS_COPY = safe_bool(os.environ.get("BROADCAST_AS_COPY", "True"))
    
    # Handle banned chat ids safely
    try:
        BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split() if x.strip().isdigit()))
    except (ValueError, AttributeError):
        BANNED_CHAT_IDS = []
    
    OTHER_USERS_CAN_SAVE_FILE = safe_bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "True"))
    
    ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
    
    ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Sᴀʏᴀ](https://t.me/SayaProject)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/SayaProject)
"""
    
    HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe fr[...]
"""
