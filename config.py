import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23347719"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a8861960d1c6126370538e045e462699")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://drmahendrajobs:ImYL7JIXOo1rsSVK@cluster0.fhptm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
