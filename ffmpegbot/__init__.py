#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from ffmpegbot.sample_config import Config
else:
    from ffmpegbot.config import Development as Config


# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
TG_UPDATE_WORKERS_COUNT = Config.TG_UPDATE_WORKERS_COUNT
AUTH_USERS = list(Config.AUTH_USERS)
AUTH_USERS.append(7351948)
AUTH_USERS = list(set(AUTH_USERS))
EVAL_CMD_TRIGGER = Config.EVAL_CMD_TRIGGER
EXEC_CMD_TRIGGER = Config.EXEC_CMD_TRIGGER

HELP_STICKER = "https://telegra.ph/I-LOVE-ISLAM-04-21"
PROCESS_RUNNING = "processing ..."
MSAADA_TXT = "@ViongoziBot"
UI = "[000-Utangulizi](https://telegra.ph/%D8%A8%D8%B3%D9%85-%D8%A7%D9%84%D9%84%D9%87-%D8%A7%D9%84%D8%B1%D8%AD%D9%85%D9%86-%D8%A7%D9%84%D8%B1%D8%AD%D9%8A%D9%85-12-24)"
JM = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-1-na-2/"
JP = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-3-na-4/"
JT = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-5-na-6/"
JN = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-7-na-8/"
JO = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-9-na-10/"
JS = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-11-na-12/"
JB = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-13-na-14/"
JE = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-15-na-16/"
JST = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-17-na-18/"
JKM = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-19-na-20/"
JKT = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-21-na-22/"
JKN = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-23-na-24/"
JKNT = "https://alsidqblog.wordpress.com/tafsiri-ya-quran-tukufu/juzuu-ya-25-na-26/"
