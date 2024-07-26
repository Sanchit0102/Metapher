#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "25570025")
API_HASH = os.environ.get("API_HASH", "62c95df09ad28778f17035b76abb3b22")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6474194755:AAFjQXYLxegqRmGxsBp3PUksxOWm3EyQ6lM") #raashi
ADMIN = int(os.environ.get("ADMIN", '1562935405'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "BOT_TESTING_OFFICIAL")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "UNF_OFFICIAL")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")    #         "mongodb+srv://UPLOADXPRO24BOT:UPLOADXPRO24BOT@cluster0.hjfk60f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002165324303')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/75dfa4b1e385a7c2d044d.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '1562935405'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1001856806130)
