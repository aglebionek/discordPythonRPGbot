import discord
import BotFunctions
import BotCommands
import BotOptions
import my_token
import re
         
class BotClient(discord.Client):
    
    
   
    async def on_ready(self):
        game = discord.Game(name = "Call of Cthulhu RPG session")
        await client.change_presence(activity=game)
        print(dir(BotFunctions))
        
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
        
        if channel.name in BotOptions.CHARACTER_CHANNELS:
            if message.attachments:
                if [0].filename.endswith(".json"):
                    await channel.send("gocha")
        
        if content.startswith(BotOptions.COMMAND_PREFIX):
            
            # remove the command symbol from the content string
            content = content[len(BotOptions.COMMAND_PREFIX):]
            
            matches = list()
            
            for command_re in BotCommands.ALL_COMMANDS.values():
                match = re.match(command_re, content)
                if match is not None: matches.append(match)
                
            if len(matches) == 0 and BotOptions.COMMAND_PREFIX != '':
                await channel.send(f"I'm sorry, command {content} doesn't match any of the commands")
                return
            elif len(matches) > 2:
                await channel.send(f"There are more than one matches found, please choose from {matches}")
                return
            else:
                # define a match variable
                match = None
            
                #region --- check for dice_roll_1 command ---
                #
                #
                
                # check if the message's content matches the command's regex
                match = re.match(BotCommands.DICE_ROLL_1, content)
                
                # if message matched the command's regex
                if match is not None: 
                    
                    # extract the size of dice from the regex
                    dice_size = int(match.group(1))
                    
                    # set default number of dice to one
                    dice_number = 1
                    
                    # if number of dice was specified
                    if match.group(2) is not None:
                        
                        # extract the number of dice from the regex
                        dice_number = int(match.group(3))
                    
                    # roll the dice and send the returned formatted string as a message to the channel
                    await channel.send(await BotFunctions.dice_roll(dice_size, dice_number))
                    return
                
                #
                #
                #endregion --- check for dice_roll_1 command ---
                
                #region --- check for dice_roll_2 command ---
                #
                #
                
                # check if the message's content matches the command's regex
                match = re.match(BotCommands.DICE_ROLL_2, content)
                
                # if message matched the command's regex
                if match is not None:
                    
                    # extract the number of dice from the regex            
                    dice_number = int(match.group(1))
                    
                    # extract the size of dice from the regex
                    dice_size = int(match.group(2))
                    
                    # roll the dice and send the returned formatted string as a message to the channel
                    await channel.send(await BotFunctions.dice_roll(dice_size, dice_number))
                    return
                
                #
                #
                #endregion --- check for dice_roll_2 command ---
                    
                #region -- check for help_command ---
                #
                #
                
                # check if the message's content matches the command's regex
                match = re.match(BotCommands.HELP_COMMAND, content)
                
                # if message matched the command's regex
                if match is not None:
                    
                    # send the returned list of commands as a message to the channel
                    await channel.send(await BotFunctions.help())
                    return
                
                #
                #
                #endregion -- check for help_command ---
                
                #region --- check for skill_test command ---
                #
                #
                
                # check if the message's content matches the command's regex
                match = re.match(BotCommands.SKILL_TEST, content)
                
                # if message matched the command's regex
                if match is not None:
                    
                    # extract the skill to test from the regex
                    skill = match.group(2)
                    
                    # send the returned formatted string as a message to the channel
                    await channel.send(await BotFunctions.test(skill))
                    return 
                
                #
                #
                #endregion --- check for skill_test command ---
            
            
if __name__ == "__main__":
    client = BotClient()
    current_token = my_token.Token()
    client.run(current_token)