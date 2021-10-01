import discord
from BotFunctions import BotFunctions
import BotCommands
import BotOptions
import my_token
import re
         
class BotClient(discord.Client):
    '''
    #region --- read options from BotOptions.py ---
    #
    #
    
    # command symbol is the sign you put at the start of a command, to let the bot knows you want it to do something
    command_symbol = BotOptions.COMMAND_SYMBOL
    
    # defines the language of the bot's responses, based in languages/channel_messages/language.json
    message_language = BotOptions.MESSAGE_LANGUAGE
    
    # defines the languages to use for character info, based in languages/character_info/language.json
    character_languages = BotOptions.CHARACTER_LANGUAGES
    
    #
    #
    #endregion end --- read options from BotOptions.py ---
    '''
   
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

        # extract the content string from discord.Message object, make it lower case and mark it as a string
        content: str = message.content.lower()
        
        # extract the channel from discord.Message object and mark it as a discord.TextChannel object
        channel: discord.TextChannel = message.channel
        
        # check if the message content is a command (it is if it starts with the command symbol)
        if content.startswith(BotOptions.COMMAND_PREFIX):
            
            # remove the command symbol from the content string
            content = content[len(BotOptions.COMMAND_PREFIX):]
            
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