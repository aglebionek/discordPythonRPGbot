import random
import re

async def dice_roll(match: re.Match) -> str:

    if match.string[0] == 'd':
        dice_size = int(match.group(2))
        dice_number = 1
        if match.group(3) is not None:
            dice_number = int(match.group(4))
    else:            
        dice_number = int(match.group(5))
        dice_size = int(match.group(6))

    a_100 = (dice_size == 100)
    
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