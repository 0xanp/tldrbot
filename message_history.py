import discord

class MessageHistory:
    def __init__(self, channels, limit=10000):
        self.channels = channels
        self.limit = limit

    async def get_messages(self, channel):
        messages = []
        async for message in channel.history(limit=self.limit):
            messages.append(message.content)
        return messages

    async def get_channel_messages(self, channel):
        messages = await self.get_messages(channel)
        return ' '.join(messages)

    async def get_text_channel_messages(self, channel):
        if isinstance(channel, discord.TextChannel):
            return await self.get_channel_messages(channel)
        return ''

    async def get_guild_messages(self, guild):
        text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]
        return {channel.name: await self.get_channel_messages(channel) for channel in text_channels}

    async def get_message_history(self):
        message_history = ''
        for channel in self.channels:
            message_history += f'{channel.name}: {await self.get_text_channel_messages(channel)}\n'
        return message_history
