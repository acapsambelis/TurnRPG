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
    

def rebuild_test_glad():
    """
        Builds and saves a fresh copy of TEST gladiator
        Used when initial gladiator values are changed and need testing
    """
    gear = Equipment(broadSwd, huntingBow, chainCP, chainLG, ironSH, chainHM, huntingQui)
    stats = Attributes("Test", 1, 10, 3, 10, 10, 10)
    glad = Player("Test", gear, stats, 10000, "Location")

    test_game = Game(None, None, None, "map.txt")
    test_game.save_glad("test", glad)


if __name__ == '__main__':
    #rebuild_test_glad()
    main()
