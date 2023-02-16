import discord
from discord.ext import commands
from history import MessageHistory
from summarize import ConversationSummarizer

client = commands.Bot(command_prefix='!')
history = MessageHistory()
summarizer = ConversationSummarizer()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command(name='tldr')
async def summarize(ctx, limit: int):
    if limit > 100:
        limit = 100
    summary_report = ''
    for channel in ctx.guild.text_channels:
        history.channel = channel
        text = await history.get_history(limit)
        if text:
            summary = summarizer.summarize(text)
            summary_report += f"\n**{channel.name}**:\n{summary}\n"
    if summary_report:
        embed = discord.Embed(title='TL;DR of the conversation in this server', description=summary_report, color=0x00ff00)
        await ctx.send(embed=embed)
    else:
        await ctx.send("There's no conversation history to summarize in this server.")

client.run('your-bot-token')
