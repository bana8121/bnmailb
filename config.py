from urllib import parse

TOKEN = "MTIzMTgwNjYzNjgwMTI2NTcyNQ.GNzGnn.C41HOPxQXqnW98axR5PvG-DSRvmz4NE3ZLDrvI"
CLIENT_SECRET = "cCowLsZ8lw7kmV9iqL_H3qBl5ueV3WiK"
REDIRECT_URI = "http://localhost:5000/oauth/callback"
OAUTH_URL = f"https://discord.com/oauth2/authorize?client_id=1231806636801265725&response_type=code&redirect_uri={parse.quote(REDIRECT_URI)}&scope=identify+guilds+email"
DISCORD = "https://discord.com/channels/@me"
