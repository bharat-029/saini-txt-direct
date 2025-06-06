#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23664819"))
API_HASH = environ.get("API_HASH", "3853f97c662d5d08cee5f0d07361361e")
BOT_TOKEN = environ.get("BOT_TOKEN", "7963498040:AAF_XBo4LIv0JzDXJvSeX_pqN5Qp4yMme5o")
OWNER = int(environ.get("OWNER", "8004315740"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '8004315740').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
