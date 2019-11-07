'''
    Main file/loop for gladiator game
'''

from gameLibrary import *
from buildItems import *
from funcLib import *

import os

def main():
    '''
        Main game file.
        Logic:
            Clears terminal
            Obtains gladiators from folder
            Prints saves for user to choose from
                Loads save into Player object
                or
                Creates new Player object
            *Loops battles* (Not final)
    '''
    os.system("CLS")
    main_game = Game()

    glad_lst = open_saves(main_game)
    
    save = write_homescreen(glad_lst)
    
    if save == -1:
        glad = main_game.create_glad()
        glad.stats.level_safe(1)
        main_game.save_glad(glad)
    else:
        glad = glad_lst[save]

    cont_loop(glad)
    

if __name__ == '__main__':
    main()
    