'''
    Main file/loop for gladiator game
'''

from charLibrary import *
from itemLibrary import *
from gameLibrary import *
from buildItems import * # Also runs file. Builds items 

def check_cont(cont):
    if go == '-1':
        return False
    else:
        return True


def main():

    # Initialize player

    player_equip = Equipment(ironSwd, chainCP, chainLG, ironSH, chainHM)
    player_stats = Attributes(0, 1, 1, 1, 1, 1)
    player = Player("Player", player_equip, player_stats, "Location")
    
    init_builder = CharacterBuilder(player)
    init_builder.level_safe(1)

    # Loop battles
    go = input("Continue?")
    cont = check_cont(go)

    while cont:

        fight = Battle(player, None, "the Thunderdome!")
        fight.main_loop()

        go = input("Continue?")
        cont = check_cont(go)
    

    
if __name__ == '__main__':
    main()