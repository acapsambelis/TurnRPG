'''
    Library of core game loading/building functions
'''

from gameLibrary import *

import os

def cont_loop(player):
    '''
        Loop leveling and battles
    '''

    go = input("Continue?")
    if go == '-1':
        cont = False
    else:
        cont = True

    while cont:

        fight = Battle(player, None, "the Thunderdome!")
        fight.confirm()

        go = input("Continue?")
        if go == '-1':
            cont = False
        else:
            cont = True


def write_homescreen(save_lst):
    print('-----------------------------------------------')
    print('                Welcome to GGG                 ')
    print('           (Generic Gladiator Game)            ')
    print('                                               ')
    print('             by Alex Capsambelis               ')
    print('-----------------------------------------------')
    print('Saves:')
    print('1: Create New')
    for i in range(len(save_lst)):
        print(i+2, ': ', save_lst[i].name, " - Level: ", \
            save_lst[i].stats.level, sep='')

    print('-----------------------------------------------')
    print("Please enter the number of the save.")
    failed = True
    while failed:
        save = input('> ')
        if save != '':
            save = int(save)
            if save in range(1, len(save_lst)+2):
                failed = False
            else:
                print("Please enter a number listed above.")
        else:
            print("Please enter a number listed above.")

    if save == 1:
        return -1
    else:
        return save - 2


def open_saves(game):
    '''
        Uses direcory /Saves
        Iterates through, making list of files to load

        returns list of gladiators
    '''

    glad_lst = list()
    for f in os.listdir("Saves"):
        glad_lst.append(game.load_glad("Saves/" + str(f)))

    return glad_lst