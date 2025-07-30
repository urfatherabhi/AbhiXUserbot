import os
from os import getenv
from dotenv import load_dotenv

# Load both .env and local.env files if present
if os.path.exists(".env"):
    load_dotenv(".env")
if os.path.exists("local.env"):
    load_dotenv("local.env")

# Required Vars
API_ID = int(getenv("API_ID", "26962851"))  # optional fallback
API_HASH = getenv("API_HASH", "06f6d4d46517e264925e245d76cb508a")  # optional fallback
BOT_TOKEN = getenv("BOT_TOKEN", "")  # Optional for userbot, required for bot
OWNER_ID = int(getenv("OWNER_ID", "0"))  # Put your owner ID or leave default
MONGO_URL = getenv("MONGO_URL", "")

# Optional Vars
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", "")
PM_LOGGER = getenv("PM_LOGGER", "")
LOG_GROUP = getenv("LOG_GROUP", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")  # Personal access token if needed
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master")  # don't change unless needed

# Pyrogram String Sessions
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

# Debug Print (Optional - Remove in Production)
# print("API_ID =", API_ID)
# print("API_HASH =", API_HASH)
# print("OWNER_ID =", OWNER_ID)
# print("SUDO_USERS =", SUDO_USERS)
