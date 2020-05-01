from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA_TXT, TMP_DOWNLOAD_DIRECTORY)

@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await bot.send_message(HELP_STICKER, reply_to_message_id=update.message_id )

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)
