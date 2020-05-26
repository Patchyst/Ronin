from gameLogic import gameLogic
from time import sleep
game_logic = gameLogic()
if game_logic.title_screen():
    sleep(1)
    game_logic.intro()
    game_logic.part_one()
else:
    exit(0)