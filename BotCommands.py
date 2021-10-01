# roll a 3,4,6,10,12,20,100 dice and optionally ad the number of dice (between 1-100)
DICE_ROLL_1 = r'^d(3|4|6|8|10|12|20|100)(\s([1-9][0-9]*|100))*$' # d[dice_size] [dice_number](optional)
#
DICE_ROLL_2 = r'^([1-9][0-9]*|100)d(3|4|6|8|10|12|20|100)$' # [dice_number]d[dice_size]

HELP_COMMAND = r'^(help|commands)$'

SKILL_TEST = r'^(t|test)\s(.*)$' # t|test [skill_name]