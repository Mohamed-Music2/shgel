from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID","16050450"))
API_HASH = getenv("API_HASH","0dd89e225b6ddd6f03e8135460d31177")
BOT_TOKEN = getenv("BOT_TOKEN","5409818512:AAHNVmbdbgAV_NBWmRl3cpU7Wpp2rWDzpz4")
SESSION_NAME = getenv("SESSION_NAME", "session","BAB-3PLsIDRarXyJ06CUFNEb14EGSTLK88inr0UlJK9d3GgSuTP4IpGcYAzmhGXr0P3j3KQZEqbj9EQ22vt3TnkawThnk3ijNSjXCbXKIaEKWTRuibJSQezppdRazoBVU7k3e7CUp2SFl42cuvTIlxocbxYqno9ehn_6KFvlL5XCBT9Uzq4rCWOQ8mNVth3hD8beHETYeE7hUPCcNh0NICv5RsstPCubms5U8sYcG4RbLmcaqqvtNuv4pk2zT3yPJXcF9muWUe434XXZjQViz4PcR7vxCNBhD4xRcmNWyIfXlSLcvjtSXsnps1ojEHxyy7xTv5vDGniimTPBZGiVJbEPAAAAAS2FcekA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME","lMl4ll")
ALIVE_NAME = getenv("ALIVE_NAME","🇩🇪ؖؖؖؖؖؖؖؖؖؖ𓆩『𖤍𝑬𝑰𝑺𝑨㉨』𝑴𝑶𝑯𝑨𝑴𝑬𝑫𓆪ؖؖؖؖؖؖؖؖؖ✹ ⃝⃙𓆩™")
BOT_USERNAME = getenv("BOT_USERNAME","lMl4ll_MUSIC_BOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lMl10l/lMl10l")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BarEisa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "D_o_m_A12")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL","mongodb+srv://shikhar:shikhar@cluster0.6xzlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("OWNER_ID","5191100896").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5191100896").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
