from urllib import parse

TOKEN = "MTIzMTgwNjYzNjgwMTI2NTcyNQ.GXxfUw.tYe9_yaQjpeBCM6zUUGkhOnZofGLZgeDeRoVJA"
CLIENT_SECRET = "bgQoC8177evTtgmRceRdkHqXxOFPM6rc"
REDIRECT_URI = "http://localhost:5000/oauth/callback"
OAUTH_URL = f"https://discord.com/oauth2/authorize?client_id=1231806636801265725&response_type=code&redirect_uri={parse.quote(REDIRECT_URI)}&scope=identify+guilds+email"
DISCORD = "https://discord.com/channels/@me"