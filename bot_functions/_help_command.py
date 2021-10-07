from BotOptions import COMMAND_PREFIX
async def help_command() -> str:
    commands = ''
    
    # dice_roll
    commands += COMMAND_PREFIX + 'd[dice_size] [dice_number](optional)\n'
    commands += COMMAND_PREFIX + '[dice_number]d[dice_size]\n'
    
    # help_command
    commands += COMMAND_PREFIX + 'help\n'
    return commands