##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQAhSnA7PzaWnJwlfWdWxir7mKp214GyKWdPHjlug1eMS8GqBPRkLJ4bhxv2tfoG4hNNeIB7VACqX-Y4y27gucZh5LNxeKm5IOiGHL9LV6XETq2Fbff2SgmxP5XGr3siJ3-n50PNkAg_9zpKXTx3ydP28-wsojIPQlLWD_po9uUclqzYtxExVjNjbZMO1xZFRV74inF7G_Gg6B1FhBXqMjKvoR9TTdzOkYseuvKOEZGv6WOtgBZfSfFSlimauTXlrKQ56k6RSYlg1uhRjwtLwgLe3v_eBSVHS6pE6VapdeojOKbePMNoIik-LK5jLuZC1QmJiNXCnqkc0Hq8mbmwpfS2AAAAAUgLerAA')
BOT_TOKEN = getenv('BOT_TOKEN', '6052195748:AAFpuknQjZ9OOnqoTKoL2515BhhneWW_ZRI')
API_ID = int(getenv("API_ID", "13976276"))
API_HASH = getenv('API_HASH', "7f024cbc744a2f44569c3641b5ccecb7")
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.flmdtda.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '6020570673').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001688479760'))
ASS_ID = int(getenv("ASS_ID", '5503679152'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '6008136265').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://te.legra.ph/file/b2258dbee2401c426eb3c.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://telegra.ph/file/cf12b3276d8b2f1aefe48.jpg")
PING_IMG = getenv('PING_IMG', "https://telegra.ph/file/85c226cce124d25c5b2ad.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', True)
