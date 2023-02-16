import discord

class MessageHistory:
    def __init__(self, channel: discord.TextChannel):
        self.channel = channel
    
    async def get_history(self, limit: int) -> str:
        messages = []
        last_id = None
        while len(messages) < limit:
            batch = await self.channel.history(limit=min(limit - len(messages), 100), before=last_id).flatten()
            if not batch:
                break
            messages.extend(batch)
            last_id = batch[-1].id
        text = '\n'.join([message.content for message in messages])
        return text
