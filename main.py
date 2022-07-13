from lib2to3.pgen2 import token
import discord
import asyncio
from discord.ext import commands
import asyncpg
import os
import ast
import playsound
from gtts import gTTS

 

bot = commands.Bot(command_prefix="n-")
client = discord.Client()


@bot.event
async def on_ready():
	print("We have logged in as {0.user}".format(bot))

@bot.command('봇과 인사를 나눈다.')
async def hi(ctx):
	await ctx.send("반가워!")
  
@bot.command()
async def test(ctx):
  await ctx.send("Thank:)")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("내가 알아 들을 수 있는 단어를 적어줘야지^^")
      
@bot.event
async def on_message(message):  
    message_content = message.content
    bad = message_content.find("--") 
    print(bad)
    if bad >= 0:
        await asyncio.sleep(300)
        await message.delete()
    await bot.process_commands(message)

@bot.command()
async def join(ctx):
    global vc
    vc = await ctx.message.author.voice.channel.connect()
    return
  
@bot.command()
async def leave(ctx):
   await ctx.voice_client.disconnect()
   return

@bot.command()
async def say(ctx, *, text):
  tts = gTTS(text=text, tld="com", lang="ko", show=False)
  tts.save("tts.mp3")
  audio.play_file('tts.mp3')
  input()

bot.run(token)