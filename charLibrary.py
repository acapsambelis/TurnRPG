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
        self.MAX_HEALTH = stats.vitality * 10 + 50
        self.health = stats.vitality * 10 + 50
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

    def __init__(self, name, gear, stats):
        super().__init__(name, gear, stats)

    def take_turn(self, other):
        '''
            Takes AI turn. If attack, random kind based on rnd
        '''
        rnd = r.randint(1,3)
        if self.health >= self.MAX_HEALTH // 2:
            self.choose_att(other, rnd)
        elif self.health < self.MAX_HEALTH // 2:
            if other.health < self.gear.weapon.dmg_h * 2:
                self.choose_att(other, rnd)
            else:
                self.heal()


class Player(Gladiator):

    def __init__(self, name, gear, stats, location):
        super().__init__(name, gear, stats)
        self.location = location

    def take_turn(self, other):
        print("0: Heal 10 hp")
        print("1: Quick attack:", self.calc_hit_chances(other, 1))
        print("2: Medium attack:", self.calc_hit_chances(other, 2))
        print("3: Heavy attack:", self.calc_hit_chances(other, 3))
        move = int(input("> "))
        while int(move) == 0:
            print("Please enter a number listed above.")
            print("Or enter '-1' to quit.")
            move = int(input(">"))
        os.system("CLS")
        self.choose_att(other, move)     


class Attibutes:

    def __init__(self, level, strength, agility, intelligence, defense, vitality):
        self.level = level
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.defense = defense
        self.vitality = vitality