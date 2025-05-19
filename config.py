import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8151035412:AAGnfaXf0-gUKtVdaPU-kUZC-VcPaJC0AA8")
    API_ID = int(os.environ.get("API_ID", "25967358"))
    API_HASH = os.environ.get("API_HASH", "10a5a31171dfdc323efdbcf84a8fb016")
    AUTH_USER = os.environ.get('AUTH_USERS', '7602994049').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
