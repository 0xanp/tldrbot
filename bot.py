import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from message_history import MessageHistory
from summarizer import Summarizer

load_dotenv()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='tldr', help='Summarize the conversation history')
async def summarize_conversation(ctx):
    message_history = MessageHistory(ctx.guild.text_channels)
    summarizer = Summarizer('transformers')
    summary = summarizer.summarize(message_history)
    if summary:
        embed = discord.Embed(title='Conversation Summary', description=summary, color=0x00ff00)
        await ctx.send(embed=embed, hidden=True)
    else:
        await ctx.send('Sorry, I was not able to generate a summary.', hidden=True)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))