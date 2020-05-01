from pyrogram import Client, Filters

from ffmpegbot import (
    HELP_STICKER,
    TMP_DOWNLOAD_DIRECTORY
)


@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def help_msaada(client, message):
    await message.reply_text(MSAADA, quote=True)
