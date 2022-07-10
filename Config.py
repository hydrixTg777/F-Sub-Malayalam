import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(749673781)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(749673781)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__ഗ്രൂപ്പിൽ പുതിയ മെംബേർസ് ജോയിൻ ചെയ്‌താൽ..... ഗ്രൂപ്പിൽ മെസ്സേജ് അയക്കാൻ ഒരു നിർദ്ദിഷ്ട ചാനലിൽ ചേരാൻ ഗ്രൂപ്പ് അംഗങ്ങളെ നിർബന്ധിക്കുക.\nനിങ്ങളുടെ ചാനലിൽ ചേർന്നിട്ടില്ലെങ്കിൽ അവരെ മ്യൂട്ട് ചെയ്യുന്നതായിരിക്കും, തുടർന്ന് അവരോട് ചാനലിൽ ചേരുകയും താഴെ കൊടുത്ത  ബട്ടൺ അമർത്തിക്കൊണ്ട് അവരെ ചാനലിൽ ചേരാനും പറയുകയും ചെയ്യും.__",
        
        """
        **ക്രമീകരണം**\n__1. ആദ്യം എന്നെ ഗ്രൂപ്പിൽ BAN USER PERMISSION ഓടു കൂടെ അഡ്മിൻ ആക്കുക.
2. ചാനലിലും എന്നെ അഡ്മിൻ ആക്കുക.\nശ്രദ്ദിക്കുക: Group creator നു മാത്രമേ എന്നെ സജ്ജീകരിക്കാൻ പറ്റൂ... 🤷‍♀️... എന്നെ അഡ്മിൻ ആക്കിയിട്ടില്ലെൽ ഞാൻ ലെഫ്റ്റ് അദിക്കും 😇.__
""",
        
        "**Commmands**\n__/FSub - നിലവിലെ settings ലഭിക്കാൻ.\n/FSub no/off/disable - ForceSubscribe ഓഫ് ആക്കുവാൻ.\n/fsub {channel username} - നിർധിഷ്ട്ട ചാനലിൽ Force Sub Enable ആക്കാൻ.\n/FSub clear - ഞാൻ മ്യുട്ട് ചെയ്ത എല്ലാവരേം അണ്മ്യുട്ട് ആക്കുവാൻ.\n\nശ്രദ്ദിക്കുക: /Forcesubscribe is an alias of /FSub__",
        
        "**Developed by @Shamielli**"
      ]

      START_MSG = """
      **Hey [{}](tg://user?id={})**\n__Hello,
This is a Malayalam Version Force Subscriber Bot by @shamilnelli 😇

Hit /help for more details.. and more thing waiting for u there__ 😉
"""
