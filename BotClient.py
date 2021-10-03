import discord
import re


import BotCommands
from bot_functions import BotFunctions
import BotOptions
import my_token

         
class BotClient(discord.Client):
    
    async def on_ready(self):
        game = discord.Game(name = "Call of Cthulhu RPG session")
        await client.change_presence(activity=game)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    
    async def on_message(self, message: discord.Message):
        
        # the bot shouldn't reply to itself
        if message.author.id == self.user.id:
            return

        # extract message content and channel from the message
        content: str = message.content.lower()
        channel: discord.TextChannel = message.channel
        
        #WIP
        if channel.name in BotOptions.CHARACTER_CHANNELS:
            if message.attachments:
                if message.attachments[0].filename.endswith(".json"):
                    await channel.send("gocha")
        
        if content.startswith(BotOptions.COMMAND_PREFIX):           
            content = content[len(BotOptions.COMMAND_PREFIX):]
            
            matches = list()
            
            for command_name, command_re in BotCommands.commands.items():
                match = re.match(command_re, content)
                if match is not None: 
                    matches.append((command_name, match))
                
            if len(matches) == 0:
                await channel.send(f"I'm sorry, command '{content}' doesn't match any of the commands.")
            elif len(matches) > 1:
                await channel.send(f"There are more than one matches found, please choose from {matches}.")
            else:
                command_name, match = matches[0]
                await channel.send(await vars(BotFunctions)[command_name](match))               

if __name__ == "__main__":
    client = BotClient()
    current_token = my_token.Token()
    client.run(current_token)