# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "27985132"))
API_HASH = getenv("API_HASH", "5bdb8f402de29b87c43f8207f751b711")
BOT_TOKEN = getenv("BOT_TOKEN", "8303614888:AAEUPKUM7EOdZeF-Ef7jfQnyccJHSYbQGvg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8114614765").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002987159907"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", 'BQGrBOwAFvvuErXqp1YGSiKfoKSg5YSthQ_jIk8LMOeqZ7oBsIO4VhsOa6ewyBrho0Prw6H0idKqdO0msiaE1_4InsIfUGA10Y5-Qr11FUhrW8HMaLZnC-JNMT-gi-vXeJeXLz4EpUg5z_bko5sDzjbGN0Eu8_5gP7bdbub8X2aIQAP3asMAM6VgI4kh4FcecPKO2XKGhVQC-hW57sIhCVhkEXiAkWd8JYafpaDw5UYuq4NHHsvONfBfMu5fXF4JXusgepZWXIzy27luXwytUXEA4YB8TD2_KY4TWkwpnCb1x8nmjes7f91VKza3W3X-qYvjmnLIiv3dXWxpWsSn41vBBn4X7wAAAAHjqzHtAA')
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
