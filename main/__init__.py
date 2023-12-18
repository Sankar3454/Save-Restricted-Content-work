#Github.com/mxsport

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=22486027, cast=int)
API_HASH = config("API_HASH", default=f5b9354db9bf76b1026d44bd6ac7813d)
BOT_TOKEN = config("BOT_TOKEN", default=6661937278:AAFO5xIp1EEuI8nCAxFdNVRBc8Rn9OS5X64)
SESSION = config("SESSION", default=BQFXHAsAlOfI2iEZbippwiKjKq6Z84BxR-Uyzcj84d5hWPi51egXlafMo3YUFfoEvhXOoY7fUTtjBYnitNCmDCikFQDO24rBi424LjSNPi3QldHHjy4zHWGClPe28jROaA3y8xkUXFtkXXwc6rt9PVcK1FP7IK7ZIVdKqgiiBLwWsbYspmmV8x2xpe9qAoVAD1UQ-T1xUUxYuOBYROnPHdgJBLgaB_3dNS3cqBcEBWX7HZvMXVRqpd2yuzgAh4ta0MlOZfXC_dBFByQ8DkYuOw3toyrqPUaVM9DhPcyFHCVy1CHZxiOEBBhgcB2k1ph85txQA4OfXzIeFwgmr8T5LMbfFmhZGAAAAABCGufmAA)
FORCESUB = config("FORCESUB", default=OTT_Walla_Bot_Support)
AUTH = config("AUTH", default=1109059558, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
