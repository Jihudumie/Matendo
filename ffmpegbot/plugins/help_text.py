from pyrogram import Client, Filters

from ffmpegbot import (HELP_STICKER, MSAADA_TXT, JM, JP, JT, JN,
JO, JS, JB, JE, JST, JKM,
JKT, JKN, JKNT)


@Client.on_message(Filters.command(["start"]))
async def start_text(client, message):
    await message.reply_text(HELP_STICKER, quote=True)

@Client.on_message(Filters.command(["help"]))
async def msaada(client, message):
    await message.reply_text(MSAADA_TXT, quote=True)

@Client.on_message(Filters.command(["01"]))
async def moja(client, message):
    await message.reply_text(JM, quote=True)

@Client.on_message(Filters.command(["02"]))
async def mbili(client, message):
    await message.reply_text(JP, quote=True)

@Client.on_message(Filters.command(["03"]))
async def tatu(client, message):
    await message.reply_text(JT, quote=True)

@Client.on_message(Filters.command(["04"]))
async def nne(client, message):
    await message.reply_text(JN, quote=True)

@Client.on_message(Filters.command(["05"]))
async def tano(client, message):
    await message.reply_text(JO, quote=True)

@Client.on_message(Filters.command(["06"]))
async def sita(client, message):
    await message.reply_text(JS, quote=True)

@Client.on_message(Filters.command(["07"]))
async def saba(client, message):
    await message.reply_text(JB, quote=True)

@Client.on_message(Filters.command(["08"]))
async def nane(client, message):
    await message.reply_text(JE, quote=True)

@Client.on_message(Filters.command(["09"]))
async def tisa(client, message):
    await message.reply_text(JTS, quote=True)

@Client.on_message(Filters.command(["10"]))
async def kumi(client, message):
    await message.reply_text(JKM, quote=True)

@Client.on_message(Filters.command(["11"]))
async def kumi_namoja(client, message):
    await message.reply_text(JKMN, quote=True)

@Client.on_message(Filters.command(["12"]))
async def kumi_nwmbili(client, message):
    await message.reply_text(JKM, quote=True)

@Client.on_message(Filters.command(["13"]))
async def kumi_natatu(client, message):
    await message.reply_text(JKT, quote=True)

@Client.on_message(Filters.command(["14"]))
async def Kumi_nne(client, message):
    await message.reply_text(JKN, quote=True)

@Client.on_message(Filters.command(["15"]))
async def kumi_tano(client, message):
    await message.reply_text(JKNT, quote=True)
