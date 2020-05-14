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

HELP_STICKER = "Karibu.\n\n1. Mimi ni Bot au Robot\n2. <u>Karibu Katika</u> @Huduma\n3. <u>Karibu katika Channel Yangu</u> @HabariTz"
MSAADA_TXT = "https://telegra.ph/I-LOVE-ISLAM-04-21"
