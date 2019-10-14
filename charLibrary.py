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
        self.position = 0

    def choose_att(self, other, decider):
        '''
            Chooses what type of attack: quick, medium, or heavy
            Calls do_dmg with damage
        '''
        rnd_divider = (self.gear.c_weapon.dmg_h - self.gear.c_weapon.dmg_l) // 3
        if decider == 0:
            self.heal()
        elif decider == 1:
            self.attack(other, self.gear.c_weapon.dmg_l, \
                self.gear.c_weapon.dmg_l + rnd_divider, \
                self.calc_hit_chances(other, decider))
        elif decider == 2:
            self.attack(other, self.gear.c_weapon.dmg_l + rnd_divider, \
                self.gear.c_weapon.dmg_l + rnd_divider * 2, \
                self.calc_hit_chances(other, decider))
        elif decider == 3:
            self.attack(other, self.gear.c_weapon.dmg_l + rnd_divider * 2, \
                self.gear.c_weapon.dmg_h, self.calc_hit_chances(other, decider))
        elif decider == 4:
            self.move(1)
        elif decider == 5:
            self.move(-1)
        elif decider == 6:
            self.change_weapon()
        elif decider == -1:
            exit()

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
        allowed = True
        if type(self.gear.c_weapon) is Bow:
            if self.gear.weapon_acc.amount > 0:
                self.gear.weapon_acc.amount -= 1
            else:
                allowed = False

        if allowed:
            if abs(self.position - other.position) <= self.gear.c_weapon.rng:
                rnd_divider = (self.gear.c_weapon.dmg_h - self.gear.c_weapon.dmg_l) // 3
                hit_damage = r.randint(lowb, highb) + self.stats.strength

                if r.randint(1, 100) < hit_chance:
                    self.do_dmg(other, hit_damage)

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
    
    def move(self, direction):
        '''
            Changes position.
            If move right, dir is positive
            If move left, dir is negative
        '''
        
        delta_x = direction * ((self.stats.agility // 2) + 1)
        if self.position + delta_x <= 50 and self.position + delta_x >= 1:
            self.position += delta_x

    def change_weapon(self):
        if self.gear.c_weapon == self.gear.weapon1:
            self.gear.c_weapon = self.gear.weapon2
        else:
            self.gear.c_weapon = self.gear.weapon1



class Opponent(Gladiator):

    def __init__(self, name, gear, stats, aggression):
        super().__init__(name, gear, stats)
        self.aggression = aggression


    def take_turn(self, other):
        '''
            Takes AI turn. If attack, random kind based on rnd
        '''
        turn_done = False
        in_range = abs(self.position - other.position) <= self.gear.c_weapon.rng
        rnd = r.randint(1,3)

        if not turn_done:
            if type(self.gear.c_weapon) is Bow and self.gear.weapon_acc.amount <= 0:
                self.change_weapon()
                turn_done = True

        if not turn_done:
            if self.aggression < 5:
                # Scaredy cat
                self.run_away(other)
                turn_done = True

        # Move towards
        if not turn_done:
            if abs(self.position - other.position) > self.gear.c_weapon.rng:
                self.run_towards(other)
            else:
                if self.health >= self.MAX_HEALTH // 2:
                    self.choose_att(other, rnd)
                else:
                    if r.randint(0, 100) > self.aggression:
                        self.choose_att(other, rnd)
                    else:
                        self.heal()

    def run_away(self, other):
        dist = (self.position - other.position)
        delta_x = (self.stats.agility // 2) + 1
        if abs(dist + delta_x) > abs(dist -1 * delta_x):
            # Move right
            self.move(1)
        else:
            # Move left
            self.move(-1)

    def run_towards(self, other):
        dist = (self.position - other.position)
        delta_x = (self.stats.agility // 2) + 1
        if abs(dist + delta_x) < abs(dist + -1 * delta_x):
            # Move right
            self.move(1)
        else:
            # Move left
            self.move(-1)



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
        print("4: Move right")
        print("5: Move left")
        if self.gear.weapon2 != None:
            print("6: Swap weapons")
        choice = input("> ")
        if choice != '':
            choice = int(choice)
        else:
            choice = -2
        while int(choice) < -1 or int(choice) > 6:
            print("Please enter a number listed above.")
            print("Or enter '-1' to quit.")
            choice = int(input(">"))
        self.choose_att(other, choice)


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
            self.level_safe(1)
            self.xp -= self.required_xp
            self.required_xp = 15 * self.level * (self.level + 5)

    def display_stats(self):
        if self.level != 1:
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
        CAP = 4
        if self.level == 0:
            CAP = 10

        # Initialize and create backup
        finished = False
        backup = Attributes(self.name, self.level, self.strength, self.agility, \
            self.intelligence, self.defense, self.vitality)
            
        # Actual Leveling
        for i in range(0, levels):
            self.level += 1
            points = 0
            while points < CAP:
                print('points:',points)
                os.system("CLS")
                self.display_stats()
                print("Please enter the number for the stat you want to increase.")
                stat = int(input('> '))
                if stat in (1, 2, 3, 4, 5):
                    self.add_stat(stat, 1)
                    points += 1
                else:
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
                
                