'''
    Gladiator class library
'''
import random as r
import os

from itemLibrary import *

class Gladiator:

    def __init__(self, name, gear, stats):
        self.name = name
        self.gear = gear
        self.stats = stats
        self.MAX_HEALTH = stats.vitality * 10 + 10
        self.health = stats.vitality * 10 + 10
        self.MAX_ARMOR = gear.totalARM
        self.armor = gear.totalARM

    def choose_att(self, other, decider):
        '''
            Chooses what type of attack: quick, medium, or heavy
            Calls do_dmg with damage
        '''
        rnd_divider = (self.gear.weapon.dmg_h - self.gear.weapon.dmg_l) // 3
        if decider == 0:
            self.heal()
        elif decider == 1:
            self.attack(other, self.gear.weapon.dmg_l, \
                self.gear.weapon.dmg_l + rnd_divider, \
                self.calc_hit_chances(other, decider))
        elif decider == 2:
            self.attack(other, self.gear.weapon.dmg_l + rnd_divider, \
                self.gear.weapon.dmg_l + rnd_divider * 2, \
                self.calc_hit_chances(other, decider))
        elif decider == 3:
            self.attack(other, self.gear.weapon.dmg_l + rnd_divider * 2, \
                self.gear.weapon.dmg_h, self.calc_hit_chances(other, decider))

    def do_dmg(self, other, amt):
        '''
            Deals damage to opponent
        '''
        if other.armor > 0:
            if other.armor > amt:
                other.armor = max(other.armor - amt, 0)
            else:
                amt -= other.armor
                other.armor = 0
                other.health = max(other.health - amt, 0)
        else:
            other.health = max(other.health - amt, 0)

    def heal(self):
        '''
            Heals self by 10 up to MAX_HEALTH
        '''
        self.health = min(self.MAX_HEALTH, self.health + 10)

    def attack(self, other, lowb, highb, hit_chance):
        '''
            Decides if and how much damage will be dealt
        '''
        rnd_divider = (self.gear.weapon.dmg_h - self.gear.weapon.dmg_l) // 3
        hit_damage = r.randint(lowb, highb) + self.stats.strength

        if r.randint(1, 100) < hit_chance:
            print(self.name, "attacks! Damage:", hit_damage)
            self.do_dmg(other, hit_damage)
        else:
            print(self.name, "missed!")

    def calc_hit_chances(self, other, att_type):
        '''
            Returns chances of the attack landing 
            based on self.stats.intelligence and other.stats.defense
        '''
        chance = 1
        if att_type == 1:
            chance = min(99, 56 + (10 * self.stats.intelligence)/other.stats.defense)
        elif att_type == 2:
            chance = min(99, 40 + (10 * self.stats.intelligence)/other.stats.defense)
        elif att_type == 3:
            chance = min(99, 23 + (10 * self.stats.intelligence)/other.stats.defense)

        return int(chance)


class Opponent(Gladiator):

    def __init__(self, name, gear, stats, aggression):
        super().__init__(name, gear, stats)
        self.aggression = aggression


    def take_turn(self, other):
        '''
            Takes AI turn. If attack, random kind based on rnd
        '''
        rnd = r.randint(1,3)
        if self.health >= self.MAX_HEALTH // 2:
            self.choose_att(other, rnd)
        else:
            if r.randint(0, 100) > self.aggression:
                self.choose_att(other, rnd)
            else:
                self.heal()



class Player(Gladiator):

    def __init__(self, name, gear, stats, location):
        super().__init__(name, gear, stats)
        self.location = location
        self.stats.level_safe(1)

    def take_turn(self, other):
        print("0: Heal 10 hp")
        print("1: Quick attack:", self.calc_hit_chances(other, 1))
        print("2: Medium attack:", self.calc_hit_chances(other, 2))
        print("3: Heavy attack:", self.calc_hit_chances(other, 3))
        move = int(input("> "))
        while int(move) < 0 or int(move) > 3:
            print("Please enter a number listed above.")
            print("Or enter '-1' to quit.")
            move = int(input(">"))
        self.choose_att(other, move)


class Attributes:

    def __init__(self, name, level, strength, agility, \
        intelligence, defense, vitality):
        self.name = name
        self.level = level
        self.xp = 0
        self.required_xp = 100
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.defense = defense
        self.vitality = vitality

    def check_level(self):
        '''
            Checks to see if the user has a level up.
            Levels up until xp is below required_xp
        '''
        while self.xp >= self.required_xp:
            self.xp -= self.required_xp
            self.level_safe(1)
            self.required_xp = 15 * self.level * (self.level + 5)

    def display_stats(self):
        print("\n-----------------------------------------------")
        print("XP: {} / {}".format(self.xp, self.required_xp))
        print("-----------------------------------------------")
        print(self.name)
        print("Level: " + str(self.level) + '\n')
        print("Strength (1):   Agility (2):   Intelligence (3):")
        print("     " + str(self.strength) + "                " + str(self.agility) \
            + "              " + str(self.intelligence))
        print("Defense (4):   Vitality (5):")
        print("     " + str(self.defense) + "                " + str(self.vitality))
        print("-----------------------------------------------\n")

    def add_stat(self, stat, amount):
        '''
            Adds stats based on an amount and a numeric value
            (Just another level of abstraction)
        '''
        if stat == 1:
            # Strength
            self.strength += amount
        elif stat == 2:
            # Agility
            self.agility += amount
        elif stat == 3:
            # Intelligence
            self.intelligence += amount
        elif stat == 4:
            # Defense
            self.defense += amount
        elif stat == 5:
            # Vitality
            self.vitality += amount

    def level_safe(self, levels):
        '''
            Levels up an Attribute set by a number
            Creates backup before changing in case the user
                wants to revert to older changes
        '''

        # Initialize and create backup
        finished = False
        backup = Attributes(self.name, self.level, self.strength, self.agility, \
            self.intelligence, self.defense, self.vitality)
            
        # Actual Leveling
        for i in range(0, levels):
            self.level += 1
            for j in range(0, 4):
                os.system("CLS")
                self.display_stats()
                print("Please enter the number for the stat you want to increase.")
                stat = int(input('> '))
                if stat in (1, 2, 3, 4, 5):
                    self.add_stat(stat, 1)
                else:
                    j += 1
                    print("Please enter a number listed above.")
        os.system("CLS")
        self.display_stats()

        # Save changes
        while not finished:
            print("Save changes? [y/n]")
            check = input('> ')
            if check == 'n':
                self = backup
                self.level_safe(levels)
                finished = True
            elif check == 'y':
                finished = True
            else:
                print("Please enter 'y' or 'n'.")
                finished = False
                
                