'''
    Class library for game/plot structures
'''

from buildItems import *
from charLibrary import *

import os
import random as r
import pickle

###############################################################################
class Title:

    def write_homescreen(self, save_lst):
        '''
            Prints out a homescreen
            Returns the number of the save to load.
                -1 if make a new save
        '''
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
            try:
                save = int(save)
                if save not in range(1, 1+len(save_lst)):
                    raise ValueError
            except:
                print("Please enter a number listed above.")
                finished = False
            else:
                if save in range(1, len(save_lst)+2):
                    failed = False
    
        if save == 1:
            return -1
        else:
            return save - 2

    def main_loop(self, game):
        '''
            Title screen main loop
                Opens saves
                Gets save to load
                Creates new gladiator or loads old gladiator
        '''
        os.system("CLS")
        glad_lst = game.open_saves()
    
        save = self.write_homescreen(glad_lst)
        
        if save == -1:
            glad = game.create_glad()
            glad.stats.level_safe(1)
            glad.update_stats()
            game.gladiator = glad
        else:
            game.gladiator = glad_lst[save]

        game.main_loop()

###############################################################################
class Game:


    def __init__(self, crh, frg, arm, map_name=""):
        self.map_str = self.build_map(map_name)
        self.gladiator = None

        self.crh = crh
        self.frg = frg
        self.arm = arm

    def open_saves(self):
        '''
            Uses direcory /Saves
            Iterates through, making list of files to load

            returns list of gladiators
        '''

        glad_lst = list()
        for f in os.listdir("Saves"):
            glad_lst.append(self.load_glad("Saves/" + str(f)))

        return glad_lst

    def build_map(self, map_name):
        '''
            Turns map file into a string
        '''
        mp = ""
        if map_name == "":
            print("None!")
            input("")

        with open("Maps/" + map_name) as f:
             for line in f:
                 mp += line

        return mp

    def create_glad(self):
        '''
            Creates and returns gladiator object
        '''
        os.system("CLS")
        print("\n-----------------------------------------------")
        print("Please enter a player name:")
        print("-----------------------------------------------")
        finished = False
        while not finished:
            name = input('> ')
            if name != '':
                finished = True
            else:
                print("Please enter a name.")
                finished = False
        gear = Equipment(bareSwd, bareAxe, bareCP, bareLG, bareSH, bareHM, None)
        stats = Attributes(name, 0, 1, 1, 1, 1, 1)
        glad = Player(name, gear, stats, 1000, "Location")

        return glad

    def load_glad(self, path):
        '''
            Loads gladiator from file
        '''
        with open(path, "rb") as f:
            decoded_data = pickle.load(f)

        return decoded_data

    def save_glad(self, savename, save):
        '''
            Saves gladiator using pickle
        '''
        filename = 'Saves/' + savename + '.glad'
        with open(filename, 'wb') as f:
            pickle.dump(save, f)

    def draw_screen(self, glad):
        '''
            Draws main map of game with gladiator stats
        '''
        os.system("CLS")
        print("\n-----------------------------------------------")
        print(glad.name + ", LVL: " + str(glad.stats.level))
        print("  XP: {} / {}".format(glad.stats.xp, \
            glad.stats.required_xp))
        print("  MONEY:", glad.money)
        print("-----------------------------------------------")
        print("HEALTH: " + str(glad.health))
        print("ARMOR: " + str(glad.armor))
        print("WEAPONS: " + str(glad.gear.weapon1.name), end='')
        if glad.gear.weapon2 is not None:
            print(",", str(glad.gear.weapon2.name), end='')
        if type(glad.gear.c_weapon) is Bow:
            print(' (' + str(glad.gear.weapon_acc.amount) + ')')
        else:
            print('')
        print("S:", glad.stats.strength, "A:", glad.stats.agility, \
            "I:", glad.stats.intelligence, "D:", glad.stats.defense,\
            "V:", glad.stats.vitality)

        print(self.map_str)


    def main_loop(self):
        '''
            Loops the main game
            Player chooses location, interacts with location, returns here
        '''
        LEAVE = -1
        move = ""
        while move != LEAVE:
            self.draw_screen(self.gladiator)
            finished = False
            while not finished:
                move = input('Location: ')
                try:
                    move = int(move)
                except:
                    print("Please enter a number listed on the map.")
                    finished = False
                else:
                    if move in (-2, -1, 1, 2, 3, 4):
                        if move == 1:
                            # Church
                            self.crh.main_loop(self.open_saves(), self.gladiator)
                        elif move == 2:
                            # Arena
                            arn = Battle(self.gladiator, None, "the Arena")
                            arn.confirm()
                        elif move == 3:
                            # Forge
                            self.frg.main_loop(self.gladiator)
                        elif move == 4:
                            # Armory
                            self.arm.main_loop(self.gladiator)
                        elif move == -2:
                            # DEV PRINT
                            print("GLADIATOR:")
                            print(self.gladiator.gear.weapon1.name)
                            input()
                        elif move == -1:
                            # Quit
                            input("Press enter to quit")
                        finished = True           

###############################################################################
class Church(Game):

    def __init__(self, map_name):
        self.map_str = self.build_map(map_name)

    def draw_church(self, glad):
        self.draw_screen(glad)

    def main_loop(self, save_lst, glad):
        self.draw_church(glad)
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
            save_names = []
            for svg in save_lst:
                save_names.append(svg.name)

            os.system("CLS")
            print("\n-----------------------------------------------")
            print("Please enter a unique save name:")
            print("-----------------------------------------------")
            finished = False
            while not finished:
                name = input('> ')
                if name != '' and name not in save_names:
                    finished = True
                    self.save_glad(name, glad)
                else:
                    print("Please enter a unique name.")
                    finished = False
        else:
            self.save_glad(save_lst[save-2].name, glad)

###############################################################################        
class Shop(Game):

    def __init__(self, map_name, stock_lsts):
        self.map_str = self.build_map(map_name)
        self.stock_lsts = stock_lsts

    def main_loop(self, glad):
        self.draw_screen(glad)
        count = 1
        stock = dict()
        for lst in self.stock_lsts:
            for item in lst:
                if item.name != "None":
                    print("  " + str(count) + ": " + str(item.price) + "g " + \
                        item.name, end=' ')
                    stock[count] = item
                    item.give_stats()
                    count += 1
            print("-----------------------------------------------")

        print("Please enter the number of the item to purchase.")
        print("  (Enter -1 to exit)")
        purchase = input("> ")
        finished = False
        while not finished:
            try:
                purchase = int(purchase)
            except:
                print("Please enter a number listed on the map.")
                finished = False
                purchase = input("> ")
            else:
                finished = True
                # Purchase
                if purchase == -1:
                    #GTFO
                    done = True
                elif glad.money >= stock[purchase].price:
                    glad.money -= stock[purchase].price
                    stock[purchase].equip(glad)
                    glad.update_stats()
                    done = False

        finished = False
        while not finished and not done:
            self.draw_screen(glad)
            print("Keep shopping? [y/n]")
            check = input('> ')
            if check == 'n':
                finished = True
            elif check == 'y':
                finished = True
                self.main_loop(glad)
            else:
                print("Please enter 'y' or 'n'.")
                finished = False

###############################################################################
class Battle:

    def __init__(self, opp1, opp2, location):
        self.cont_fight = True
        self.opp1 = opp1
        self.name_lst = self.build_name_lst('Ref/names.txt')

        if opp2 != None:
            self.opp2 = opp2
        else:
            lvl_low = max(1, opp1.stats.level - r.randint(0, 2))
            lvl_high = opp1.stats.level + r.randint(0, 1)
            self.opp2 = self.gen_rnd_glad(r.randint(lvl_low, lvl_high), \
                self.name_lst[r.randint(0, len(self.name_lst) - 1)])

        self.opp1.position = 18
        self.opp2.position = 32
        self.location = location
        self.play_field = ['|'] + [' '] * 50 + ['|']


    def build_name_lst(self, filename):
        '''
            Creates a list of names given the file. File should be Ref/names.txt
        '''
        name_lst = []
        f = open(filename)
        for line in f:
            name_lst += [line.strip()]

        f.close()

        return name_lst

    def gen_rnd_glad(self, lvl, name):
        '''
            Randomly distributes points among attributes
            Takes level of enemy
            Gives 4 points per level
            Randomly distributes points for gear. Lvl - random buffer
        '''
        atb = [1, 1, 1, 1, 1]
        rnd_buffer = r.randint(0, lvl-1)
        for i in range(lvl*4, 0, -1):
            rnd_atb = r.randint(0, len(atb)-1)
            atb[rnd_atb] += 1

        gear_lst = [1, 1, 0, 0, 0, 0, 0]

        rnd_1 = r.random()
        if rnd_1 > .6:
            weaponLst1 = swordLst
        elif rnd_1 > .3:
            weaponLst1 = axeLst
        else:
            weaponLst1 = bowLst

        rnd_2 = r.random()
        if weaponLst1 != bowLst:
            if rnd_2 > .75:
                weaponLst2 = swordLst
            elif rnd_2 > .5:
                weaponLst2 = axeLst
            elif rnd_2 > .25:
                weaponLst2 = bowLst
            else:
                weaponLst2 = [None]
                gear_lst[1] = 0
        else:
            if rnd_2 > .5:
                weaponLst2 = swordLst
            else:
                weaponLst2 = axeLst

        weaponLst3 = accessLst[0]
        if weaponLst2 == bowLst or weaponLst1 == bowLst:
            weaponLst3 = accessLst[1]
            gear_lst[6] += 1

        gear_master = [weaponLst1, weaponLst2, chestLst, legLst, \
            shieldLst, helmetLst, weaponLst3]

        for i in range(3 * (lvl - rnd_buffer), 0, -1):
            length = len(gear_lst) - 1
            if gear_lst[6] == 0:
                length = len(gear_lst) - 2
            rnd_gear = r.randint(0, length)
            if gear_lst[rnd_gear] + 1 < len(gear_master[rnd_gear]):
                gear_lst[rnd_gear] += 1
            else:
                i += 1
                
        att = Attributes(name, lvl, atb[0], atb[1], atb[2], atb[3], atb[4])
        gear = Equipment(weaponLst1[gear_lst[0]], weaponLst2[gear_lst[1]], \
            chestLst[gear_lst[2]], legLst[gear_lst[3]], shieldLst[gear_lst[4]], \
            helmetLst[gear_lst[5]], weaponLst3[gear_lst[6]])

        agg = r.randint(0, 100)

        return Opponent(name, gear, att, agg)

    def restart(self):
        '''
            Resets battle and competitors
        '''
        self.opp1.health = self.opp1.MAX_HEALTH
        self.opp2.health = self.opp2.MAX_HEALTH
        self.opp1.armor = self.opp1.MAX_ARMOR
        self.opp2.armor = self.opp2.MAX_ARMOR

        if self.opp1.gear.weapon_acc != None:
            self.opp1.gear.weapon_acc.amount = self.opp1.gear.weapon_acc.MAX_CAPACITY
        if self.opp2.gear.weapon_acc != None:
            self.opp2.gear.weapon_acc.amount = self.opp2.gear.weapon_acc.MAX_CAPACITY

        self.write_status()

    def confirm(self):
        self.write_status()
        finished = False
        while not finished:
            print("Enter battle? [y/n]")
            check = input('> ')
            if check == 'n':
                finished = True
            elif check == 'y':
                finished = True
                self.main_loop()
            else:
                print("Please enter 'y' or 'n'.")
                finished = False


    def main_loop(self):
        '''
            Main loop for battle. Stops looping when someone dies (HP <= 0)
        '''
        self.restart()

        while self.cont_fight:
            self.opp1.take_turn(self.opp2)

            self.write_status()
            self.check_healths()
            if not self.cont_fight:
                break

            self.opp2.take_turn(self.opp1)
            self.write_status()
            self.check_healths()

        self.give_result()

    def write_status(self):
        '''
            Prints out health and armor
        '''
        os.system("CLS")
        print("\n-----------------")
        print(self.opp1.name + "      Level: " + str(self.opp1.stats.level))
        print("HEALTH: " + str(self.opp1.health))
        print("ARMOR: " + str(self.opp1.armor))
        print("WEAPON: " + str(self.opp1.gear.c_weapon.name), end='')
        if type(self.opp1.gear.c_weapon) is Bow:
            print(' (' + str(self.opp1.gear.weapon_acc.amount) + ')')
        else:
            print('')
        print("S:", self.opp1.stats.strength, "A:", self.opp1.stats.agility, \
            "I:", self.opp1.stats.intelligence, "D:", self.opp1.stats.defense,\
            "V:", self.opp1.stats.vitality)

        print("\n-----------------")

        print(self.opp2.name + "      Level: " + str(self.opp2.stats.level))
        print("HEALTH: " + str(self.opp2.health))
        print("ARMOR: " + str(self.opp2.armor))
        print("WEAPON: " + str(self.opp2.gear.c_weapon.name), end='')
        if type(self.opp2.gear.c_weapon) is Bow:
            print(' (' + str(self.opp2.gear.weapon_acc.amount) + ')')
        else:
            print('')
        print("S:", self.opp2.stats.strength, "A:", self.opp2.stats.agility, \
            "I:", self.opp2.stats.intelligence, "D:", self.opp2.stats.defense,\
            "V:", self.opp2.stats.vitality)
        print("-------------------")
        self.show_positions()

    def show_positions(self):
        
        #Reset play_field
        self.play_field = ['|'] + [' '] * 50 + ['|']

        self.play_field[self.opp1.position] = self.opp1.name[:1]
        self.play_field[self.opp2.position] = self.opp2.name[:1]

        # Draw play_field
        print("\n----------------------------------------------------")
        print(*self.play_field, sep='')
        print("----------------------------------------------------\n")


    def check_healths(self):
        '''
            Makes sure everyone is still alive
        '''
        if self.opp1.health <= 0 or self.opp2.health <= 0:
            self.cont_fight = False
        else:
            self.cont_fight = True

    def give_result(self):
        '''
            Who lives, who dies, who tells your story
        '''
        if self.opp1.health <= 0:
            print("{} has been slain!".format(self.opp1.name))
            if type(self.opp2) is Player:
                self.opp2.stats.xp += 30 * self.opp1.stats.level + r.randint(0, 15)
                self.opp2.stats.check_level()
                self.opp2.update_stats()
        elif self.opp2.health <= 0:
            print("{} has been slain!".format(self.opp2.name))
            if type(self.opp1) is Player:
                self.opp1.stats.xp += 30 * self.opp1.stats.level + r.randint(0, 15)
                self.opp1.stats.check_level()
                self.opp1.update_stats()
