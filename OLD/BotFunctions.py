import random
import json
import re
import math
import BotOptions

class BotFunctions():
    '''
    This class contains functions that provide functionality to the commands
    '''
    
    @staticmethod
    async def dice_roll(dice_size: int, dice_number: int) -> str:
        a_100 = dice_size == 100
        
        async def roll(dice_size: int):
            if not a_100:
                return random.randrange(1, dice_size+1)
            else:
                tens = random.randrange(0, 100, 10)
                ones = random.randrange(1, 11)
                return tuple((tens, ones))
            
        results = [await roll(dice_size) for _ in range(dice_number)]
        
        if not a_100:
            results_sum = sum(results)
        else:
            results_sum = 0
            for roll in results:
                results_sum += roll[0] + roll[1]
                
        return f"```python\n{results_sum}\nDetails: {results}```"
    
    @staticmethod
    async def help() -> str:
        commands = ''
        commands += '!d[dice_size] [dice_number](optional)\n'
        commands += '![dice_number]d[dice_size]\n'
        commands += '!help\n'
        return commands
    
    @staticmethod
    async def create_player():
        pass
    
    @staticmethod
    async def test(skill_to_test) -> str:
        with open("./languages/character_info/pl.json", encoding='utf-8') as file:
            data = json.load(file)
            matches = []
            for index in range(5, len(data)):
                name = data[str(index)]
                search = re.search(r'^' + re.escape(skill_to_test), name)
                if search is not None: matches.append(name)
            
            if len(matches) > 1:
                return f"There are more than one matches found, please choose from {matches}"
            elif len(matches) < 1:
                return "Sorry, no matching skill found"
            else:
                value = 50
                tens = random.randrange(0, 100, 10)
                ones = random.randrange(1, 11)
                roll = tens+ones
                text = f"{tens, ones} {roll}/{value} " 

                if roll <= value:
                    if roll == 1:
                        text += "critical success" 
                    elif roll <= math.floor(value/5):
                        text += "extreme success"
                    elif roll <= math.floor(value/2):
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
                return text
            
                    