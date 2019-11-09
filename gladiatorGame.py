'''
    Main file/loop for gladiator game
'''

from gameLibrary import *


def main():
    '''
        Main game file.
        Logic:
            Clears terminal
            Builds locations in map
            Runs Title.main_loop
                Loads correct gladiator
                Player enters town, can go to different places
                    inside main_game.main_loop()
    '''

    crh = Church("church.txt")
    frg = Shop("forge.txt", [swordLst, axeLst, bowLst, quiverLst])
    arm = Shop("armory.txt", [chestLst, legLst, shieldLst, helmetLst])

    main_game = Game(crh, frg, arm, "map.txt")
    title_screen = Title()

    title_screen.main_loop(main_game)
    

if __name__ == '__main__':
    main()
    