from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA_TXT, TMP_DOWNLOAD_DIRECTORY, UTANGULIZI)
4

@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["011"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)

@Client.on_message(Filters.command(["000"]))
async def uta_ngu(client, message):
    await message.reply_text(UTANGULIZI, quote=True)
