'''
    Library for weapon and armor classes
'''

class Equipment:

    def __init__(self, weapon, chest, legs, shield, helmet):
        self.weapon = weapon
        self.chest = chest
        self.legs = legs
        self.shield = shield
        self.helmet = helmet
        self.totalARM = chest.armor_val + legs.armor_val + shield.armor_val \
            + shield.armor_val + helmet.armor_val


class Sword(Equipment):
    
    def __init__(self, name, dmg_l, dmg_h, rng):
        self.name = name
        self.dmg_l = dmg_l
        self.dmg_h = dmg_h
        self.rng = rng

    def bleedDMG(self, victim):
        pass


class Axe(Equipment):
    
    def __init__(self, name, dmg_l, dmg_h, rng):
        self.name = name
        self.dmg_l = dmg_l
        self.dmg_h = dmg_h
        self.rng = rng

    def gashDMG(self, victim):
        pass


class Chestplate(Equipment):

    def __init__(self, name, armor_val):
        self.name = name
        self.armor_val = armor_val


class Legs(Equipment):

    def __init__(self, name, armor_val):
        self.name = name
        self.armor_val = armor_val


class Shield(Equipment):

    def __init__(self, name, armor_val):
        self.name = name
        self.armor_val = armor_val


class Helmet(Equipment):

    def __init__(self, name, armor_val):
        self.name = name
        self.armor_val = armor_val