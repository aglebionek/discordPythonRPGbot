import json
import math
import random
import re


import BotOptions


#WIP
async def skill_test(match: re.Match) -> str:
    matches = []
    
    for language in BotOptions.CHARACTER_LANGUAGES:
        with open(f"./materials/{language}.json", encoding='utf-8') as file:
            data: dict = json.load(file)
            
            dict_keys = list(data)
            dict1 = data[dict_keys[0]]
            dict2 = data[dict_keys[1]]
            if len(dict1) > len(dict2): data = dict1
            else: data = dict2
            
            skill_to_test = match.group(2)
            
            for skill_name, skill_value in data.items():
                search = re.search(r'' + re.escape(skill_to_test), skill_name)
                if search is not None: 
                    matches.append((skill_name, skill_value))
            
    if len(matches) > 1:
        return f"There are more than one matches found, please choose from {matches}"
    elif len(matches) < 1:
        return "Sorry, no matching skill found"
    else:
        skill_name, skill_value = matches[0]
        
        tens = random.randrange(0, 100, 10)
        ones = random.randrange(1, 11)
        roll = tens+ones
        text = f"{skill_name} {tens, ones} {roll}/{skill_value} " 

        if roll <= skill_value:
            if roll == 1:
                text += "critical success" 
            elif roll <= math.floor(skill_value/5):
                text += "extreme success"
            elif roll <= math.floor(skill_value/2):
                text += "hard success"
            else:
                text += "success"
        else:
            text += "fail "
            if skill_value < 50:
                if roll >= 96:
                    text += "(misfortune)"
            else:
                if roll >= 99:
                    text += "(misfortune)"
        return text