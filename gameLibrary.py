'''
    Class library for game/plot structures
'''

from buildItems import *
from charLibrary import *
import os

import random as r

class GameSave:

    def __init__(self):
        pass

    def build_name_lst(filename):
        '''
            Creates a list of names given the file. File should be names.txt
        '''
        name_lst = []
        for line in open(filename):
            name_lst += [line.strip()]

        return name_lst

    name_lst = build_name_lst('names.txt')


class CharacterBuilder(GameSave):

    def __init__(self, character):
        self.character = character

    def display_stats(self):
        print("\n-----------------------------------------------")
        print(self.character.name)
        print("Level: " + str(self.character.stats.level) + '\n')
        print("Strength (1):   Agility (2):   Intelligence (3):")
        print("     " + str(self.character.stats.strength) \
            + "                " + str(self.character.stats.agility) \
            + "              " + str(self.character.stats.intelligence))
        print("Defense (4):   Vitality (5):")
        print("     " + str(self.character.stats.defense) \
             + "                " + str(self.character.stats.vitality))
        print("-----------------------------------------------\n")

    def add_stat(self, stat, amount):
        if stat == 1:
            # Strength
            self.character.stats.strength += amount
        elif stat == 2:
            # Agility
            self.character.stats.agility += amount
        elif stat == 3:
            # Intelligence
            self.character.stats.intelligence += amount
        elif stat == 4:
            # Defense
            self.character.stats.defense += amount
        elif stat == 5:
            # Vitality
            self.character.stats.vitality += amount

    def level_up(self, levels):
        self.character.stats.level += levels
        failed = False
        for i in range(0, levels):
            for j in range(0, 4):
                os.system("CLS")
                if failed:
                    print("Please enter a number listed above.")
                self.display_stats()
                print("Please enter the number for the stat you want to increase.")
                stat = int(input('> '))
                if stat in (1, 2, 3, 4, 5):
                    self.add_stat(stat, 1)
                else:
                    j += 1
                    failed = True

    def level_safe(self, levels):
        backup = self.character.stats
        self.level_up(levels)
        finished = False
        while not finished:
            print("Save changes? [y/n]")
            check = input('> ')
            if check == 'n':
                self.character.stats = backup
                finished = True
                print("Changes reverted.")
            elif check == 'y':
                finished = True
            else:
                print("Please enter 'y' or 'n'.")
                finished = False


class Shop(GameSave):

    def __init__(self, character):
        self.character = character


class Battle(GameSave):

    def __init__(self, opp1, opp2, location):
        super().__init__()
        self.cont_fight = True
        self.opp1 = opp1

        if opp2 != None:
            self.opp2 = opp2
        else:
            lvl_low = max(1, opp1.stats.level - r.randint(0, 2))
            lvl_high = opp1.stats.level + r.randint(0, 2)
            self.opp2 = self.gen_rnd_glad(r.randint(lvl_low, lvl_high), \
                super().name_lst[r.randint(0, len(super().name_lst) - 1)])

        self.location = location

    def gen_rnd_glad(self, lvl, name):
        '''
            Randomly distributes points among attributes
            Takes level of enemy
            Gives 4 points per level
            Randomly distributes points for gear. Lvl - random buffer
        '''
        atb = [1, 1, 1, 1, 1]
        rnd_buffer = r.randint(0, lvl)
        for i in range(lvl*4, 0, -1):
            rnd_atb = r.randint(0, len(atb)-1)
            atb[rnd_atb] += 1

        if r.random() > .5:
            weaponLst = swordLst
        else:
            weaponLst = axeLst

        gear_master = [weaponLst, chestLst, legLst, shieldLst, helmetLst]
        gear_lst = [0, 0, 0, 0, 0]
        for i in range(lvl - rnd_buffer, 0, -1):
            rnd_gear = r.randint(0, len(gear_lst)-1)
            if gear_lst[rnd_gear] + 1 < len(gear_master[rnd_gear]):
                gear_lst[rnd_gear] += 1
            else:
                i += 1

        att = Attributes(lvl, atb[0], atb[1], atb[2], atb[3], atb[4])
        gear = Equipment(weaponLst[gear_lst[0]], chestLst[gear_lst[1]], \
            legLst[gear_lst[2]], shieldLst[gear_lst[3]], helmetLst[gear_lst[4]])
        return Opponent(name, gear, att)

    def restart(self):
        '''
            Resets battle and competitors
        '''
        print("Welcome to", self.location, "\n")
        self.opp1.health = self.opp1.MAX_HEALTH
        self.opp2.health = self.opp2.MAX_HEALTH
        self.opp1.armor = self.opp1.MAX_ARMOR
        self.opp2.armor = self.opp2.MAX_ARMOR
        self.write_status()

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
        print("S:", self.opp1.stats.strength, "A:", self.opp1.stats.agility, \
            "I:", self.opp1.stats.intelligence, "D:", self.opp1.stats.defense,\
            "V:", self.opp1.stats.vitality)
        print("\n-----------------")
        print(self.opp2.name + "      Level: " + str(self.opp2.stats.level))
        print("HEALTH: " + str(self.opp2.health))
        print("ARMOR: " + str(self.opp2.armor))
        print("S:", self.opp2.stats.strength, "A:", self.opp2.stats.agility, \
            "I:", self.opp2.stats.intelligence, "D:", self.opp2.stats.defense,\
            "V:", self.opp2.stats.vitality)
        print("-------------------")

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
        elif self.opp2.health <= 0:
            print("{} has been slain!".format(self.opp2.name))
            