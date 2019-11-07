'''
    Library for weapon and armor classes
'''

class Equipment:

    def __init__(self, weapon1, weapon2, chest, legs, shield, helmet, weapon_acc):
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.c_weapon = weapon1

        self.chest = chest
        self.legs = legs
        self.shield = shield
        self.helmet = helmet
        self.weapon_acc = weapon_acc

        self.totalARM = chest.armor_val + legs.armor_val + shield.armor_val \
            + shield.armor_val + helmet.armor_val


# Weapons

class Weapon:

    def __init__(self, name, dmg_l, dmg_h, rng):
        self.name = name
        self.dmg_l = dmg_l
        self.dmg_h = dmg_h
        self.rng = rng


class Sword(Weapon):

    def __init__(self, name, dmg_l, dmg_h, rng):
        super().__init__(name, dmg_l, dmg_h, rng)


class Axe(Weapon):
    
    def __init__(self, name, dmg_l, dmg_h, rng):
        super().__init__(name, dmg_l, dmg_h, rng)


class Bow(Weapon):

    def __init__(self, name, dmg_l, dmg_h, rng):
        super().__init__(name, dmg_l, dmg_h, rng)


class Accesory:

    def __init__(self, name):
        self.name = name


class Quiver(Accesory):

    def __init__(self, name, amount):
        super().__init__(name)
        self.MAX_CAPACITY = amount
        self.amount = amount

# Armor

class Armor:

    def __init__(self, name, armor_val):
        self.name = name
        self.armor_val = armor_val


class Chestplate(Armor):

    def __init__(self, name, armor_val):
        super().__init__(name, armor_val)


class Legs(Armor):

    def __init__(self, name, armor_val):
        super().__init__(name, armor_val)


class Shield(Armor):

    def __init__(self, name, armor_val):
        super().__init__(name, armor_val)


class Helmet(Armor):

    def __init__(self, name, armor_val):
        super().__init__(name, armor_val)