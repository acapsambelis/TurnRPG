'''
    Main file/loop for gladiator game
'''

from charLibrary import *
from itemLibrary import *
from gameLibrary import *
from buildItems import * # Also runs file. Builds items 

def check_cont(cont):
    if cont == '-1':
        return False
    else:
        return True


def main():

    # Initialize player

    player_equip = Equipment(longBow, ironSwd, chainCP, chainLG, \
        ironSH, chainHM, huntingQui)
    player_stats = Attributes("Player", 0, 1, 1, 1, 1, 1)
    player = Player("Player", player_equip, player_stats, "Location")

    # Loop battles
    go = input("Continue?")
    cont = check_cont(go)

    while cont:

        fight = Battle(player, None, "the Thunderdome!")
        fight.confirm()

        go = input("Continue?")  
        cont = check_cont(go)

    
if __name__ == '__main__':
    main()
