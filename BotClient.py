import discord
import json
import re


import BotCommands
from bot_functions import BotFunctions
import BotOptions
import my_token

with open("./BotCommands.json", encoding='utf-8') as file:
    commands: dict = json.load(file)
    
with open("./BotOptions.json", encoding='utf-8') as file:
    options: dict = json.load(file)
    
functions = vars(BotFunctions)

current_campaign = options["CURRENT_CAMPAIGN"]

with open(f"./campaigns/{current_campaign}.json", encoding='utf-8') as file:
    campaign_data: dict = json.load(file)

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
        if channel.name in options["CHARACTER_CHANNELS"]:
            if message.attachments:
                if message.attachments[0].filename.endswith(".json"):
                    print(message.attachments[0])
                    await channel.send(await BotFunctions.create_player(message.attachments[0], message.author.id, current_campaign))
        
        if content.startswith(options["COMMAND_PREFIX"]):           
            content = content[len(options["COMMAND_PREFIX"]):]
            
            matches = list()
            
            for command_name, command_re in commands.items():
                match = re.match(command_re, content)
                if match is not None: 
                    matches.append((command_name, match))
                
            if len(matches) == 0:
                await channel.send(f"I'm sorry, command '{content}' doesn't match any of the commands.")
            elif len(matches) > 1:
                await channel.send(f"There are more than one matches found, please choose from {[match[0] for match in matches]}.")
            else:
                command_name, match= matches[0]
                if command_name == 'dice_roll':
                    await channel.send(await functions[command_name](match))
                elif command_name == 'help_command':
                    await channel.send(await functions[command_name]())
                elif command_name == 'skill_test':
                    await channel.send(await functions[command_name](match))
                elif command_name == 'create_campaign':
                    await channel.send(await functions[command_name](match))

                    
                
                
if __name__ == "__main__":
    client = BotClient()
    current_token = my_token.Token()
    client.run(current_token)