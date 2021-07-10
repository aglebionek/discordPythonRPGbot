import discord
from random import randrange
from player import Player
import pickle
import os.path
from math import floor
from ast import literal_eval
import my_token

class DiceClass:

    @staticmethod
    async def RollDice(message):
        # !d[dieSize] [numberOfDice]
        msg = message.content

        # if there is no space ' ', that means only one die is rolled
        if ' ' not in msg:
            dieSize = int(msg[2:])
            dieResult = await DiceClass.Roll(dieSize)
            await message.channel.send(f'{dieResult} thee got, on thy {dieSize} sided die...')
        else:
            for i in range(2, len(msg)):
                if msg[i] == ' ':
                    dieSize = int(msg[2:i])
                    diceNumber = int(msg[i:])
                    break

            diceResults = [await DiceClass.Roll(dieSize) for x in range(0, diceNumber)]
            print(diceResults)
            if dieSize != 100:
                diceResultsSum = sum(diceResults)
            else:
                diceResultsSum = 0
                for obj in diceResults:
                    diceResultsSum += obj[0] + obj[1]
            await message.channel.send(f'{diceResults} [{diceResultsSum}] are thy {diceNumber} throws...')

    @staticmethod
    async def Roll(size):
        if size == 100:
            tens = randrange(0, 100, 10)
            ones = randrange(1, 11)
            return tuple((tens, ones))
        else:
            return randrange(1, size+1)


class PlayersClass:
    players = dict()
    if os.path.isfile("./players.pickle"):
        with open('players.pickle', 'rb') as file:
            players = pickle.load(file)
    

    @staticmethod
    async def InitPlayer(message, **kwargs):
        if message.author.id not in PlayersClass.players:
            if "lang" in kwargs.keys():
                PlayersClass.players[message.author.id] = Player(lang = kwargs["lang"])
            else:
                PlayersClass.players[message.author.id] = Player(lang = "pl")
            await message.channel.send(f"Character for player {message.author.name} created")
            with open('players.pickle', 'wb') as file:
                pickle.dump(PlayersClass.players, file)
        else:
            await message.channel.send(f"Character for player {message.author.name} already exists")

    @staticmethod
    async def PlayerStats(message):
        if message.author.id in PlayersClass.players:
            p = PlayersClass.players[message.author.id]
            await message.channel.send(await p.list())
        else:
            await message.channel.send(f"User {message.author.name} did not !init a player")

    @staticmethod
    async def UpdateStats(message):
        if message.author.id in PlayersClass.players:
            msg = message.content[5:]
            attr = str()
            value = None

            if ' ' not in msg:
                await message.channel.send(f"The command should look like !set [stat] [value], without the brackets")
                pass
            else:
                for i in range(0, len(msg)):
                    if msg[i] == ' ':
                        attr = msg[:i].lower()
                        value = msg[i+1:]
                        break

            if attr in PlayersClass.players[message.author.id].__dict__.keys():
                PlayersClass.players[message.author.id].__dict__[attr] = int(value)

                with open('players.pickle', 'wb') as file:
                    pickle.dump(PlayersClass.players, file)

                await message.channel.send(f"Succesfully set {attr} to {value}")
                if attr == 'zręczność':
                    PlayersClass.players[message.author.id].__dict__['zręczność'] = int(value)/2
                elif attr == 'edukacja':
                    PlayersClass.players[message.author.id].__dict__['język ojczysty'] = int(value)
                elif attr == 'dexterity':
                    PlayersClass.players[message.author.id].__dict__['dodge'] = int(value)/2
                elif attr == 'education':
                    PlayersClass.players[message.author.id].__dict__['language'] = int(value)
                    
            else:
                await message.channel.send(f"No stat named {attr}")  
        
    @staticmethod
    async def RemovePlayer(message):
        if message.author.id in PlayersClass.players:
            PlayersClass.players.pop(message.author.id)

            with open('players.pickle', 'wb') as file:
                pickle.dump(PlayersClass.players, file)
            await message.channel.send(f"Character for player {message.author.name} removed")

    @staticmethod
    async def SkillTest(message):
        attr = message.content[6:]

        if attr in PlayersClass.players[message.author.id].__dict__.keys():
            value = int(PlayersClass.players[message.author.id].__dict__[attr])
            tens, ones = await DiceClass.Roll(100)
            roll = tens+ones
            text = f"{tens, ones} {roll}/{value} " 

            if roll <= value:
                if roll == 1:
                    text += "critical success" 
                elif roll <= floor(value/5):
                    text += "extreme success"
                elif roll <= floor(value/2):
                    text += "hard success"
                else:
                    text += "success"
            else:
                text += "fail "
                if value < 50:
                    if roll >= 96:
                        text += "(misfortune)"
                else:
                    if roll >= 99:
                        text += "(misfortune)"
            await message.channel.send(text)
        else:
            await message.channel.send("No such attribute")

    @staticmethod
    async def Fullset(message):
        msg = message.content[9:]
        PlayersClass.players[message.author.id].__dict__ = literal_eval(msg)

class HelpingClass():

    @staticmethod
    async def Help(message):
        commands = "!d[dieSize] [dieNumber] - roll a dice\n!init - create a character for discord user with stats in polish\n!initeng - create a character for discord user with stats in english\n!stats - list characters statistic\n!set [statistic] [value] - set a character's statistic\n!remove - removes your character\n!test [statistic] - perform a statstic's test\n!fullset [statistics dictionary] - replace all statstics with provided dictionary\n!help - display this message"
        await message.channel.send(commands)
            

class MyClient(discord.Client):
   
    async def on_ready(self):
        game = discord.Game(name = "Call of Cthulhu RPG session")
        await client.change_presence(activity=game)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        elif message.content.lower().startswith('!d'):
            await DiceClass.RollDice(message)

        elif message.content == '!init':
            await PlayersClass.InitPlayer(message)

        elif message.content.lower() =='!initeng':
            await PlayersClass.InitPlayer(message, lang="eng")

        elif message.content.startswith('!stats'):
            await PlayersClass.PlayerStats(message)

        elif message.content.startswith('!set'):
            await PlayersClass.UpdateStats(message)

        elif message.content.startswith('!remove'):
            await PlayersClass.RemovePlayer(message)

        elif message.content.startswith('!test'):
            await PlayersClass.SkillTest(message)

        elif message.content.startswith('!fullset'):
            await PlayersClass.Fullset(message)
        
        elif message.content.startswith('!help'):
            await HelpingClass.Help(message)

client = MyClient()
current_token = my_token.Token()
client.run(current_token)