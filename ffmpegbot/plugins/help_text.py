from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA_TXT, TMP_DOWNLOAD_DIRECTORY, UTAN_GULIZI)
4

@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)

@Client.on_message(Filters.command(["000"]))
async def utangulizi(client, message):
    await message.reply_text(UTAN_GULIZI, quote=True)
