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
        self.MAX_HEALTH = stats.vitality * 10
        self.health = stats.vitality * 10
        self.MAX_ARMOR = gear.totalARM
        self.armor = gear.totalARM

    def attack(self, other):
        dam_ammount = r.randint(0, self.stats.strength) + self.gear.weapon.dmg
        print(dam_ammount)
        if other.armor > 0:
            if other.armor > dam_ammount:
                other.armor = max(other.armor - dam_ammount, 0)
            else:
                dam_ammount -= other.armor
                other.armor = 0
                other.health = max(other.health - dam_ammount, 0)
        else:
            other.health = max(other.health - dam_ammount, 0)

    def heal(self):
        self.health = min(self.MAX_HEALTH, self.health + 10)


class Opponent(Gladiator):

    def __init__(self, name, gear, stats):
        super().__init__(name, gear, stats)

    def take_turn(self, other):
        if self.health >= self.MAX_HEALTH // 2:
            self.attack(other)
            print(self.name, "attacks!")
        elif self.health < self.MAX_HEALTH // 2:
            if other.health < self.gear.weapon.dmg * 2:
                self.attack(other)
                print(self.name, "attacks!")
            else:
                self.heal()
                print(self.name, "heals!")


class Player(Gladiator):

    def __init__(self, name, gear, stats, location):
        super().__init__(name, gear, stats)
        self.location = location

    def take_turn(self, other):
        move = int(input("0 = Heal, 1 = Attack: "))
        if move == 0:
            self.heal()
        elif move == 1:
            self.attack(other)


class Battle:

    def __init__(self, opp1, opp2, location):
        self.cont_fight = True
        self.opp1 = opp1
        self.opp2 = opp2
        self.location = location


    def restart(self):
        print("Welcome to", self.location, "\n")
        self.opp1.health = self.opp1.MAX_HEALTH
        self.opp2.health = self.opp2.MAX_HEALTH
        self.opp1.armor = self.opp1.MAX_ARMOR
        self.opp2.armor = self.opp2.MAX_ARMOR
        self.write_health(False)

    def begin(self):
        self.restart()

        while self.cont_fight:
            self.opp1.take_turn(self.opp2)

            self.write_health(True)
            self.check_healths()
            if not self.cont_fight:
                break

            self.opp2.take_turn(self.opp1)
            self.write_health(True)
            self.check_healths()

        self.give_result()

    def write_health(self, clear):
        if clear:
            os.system("cls")
        print("\n-----------------")
        print(self.opp1.name + " HP: " + str(self.opp1.health))
        print("ARMOR: " + str(self.opp1.armor))
        print(self.opp2.name + " HP: " + str(self.opp2.health))
        print("ARMOR: " + str(self.opp2.armor))
        print("-----------------")

    def check_healths(self):
        if self.opp1.health <= 0 or self.opp2.health <= 0:
            self.cont_fight = False
        else:
            self.cont_fight = True

    def give_result(self):
        if self.opp1.health <= 0:
            print("{} has been slain!".format(self.opp1.name))
        elif self.opp2.health <= 0:
            print("{} has been slain!".format(self.opp2.name))


class Attibutes:

    def __init__(self, strength, agility, intelligence, defense, vitality):
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.defense = defense
        self.vitality = vitality