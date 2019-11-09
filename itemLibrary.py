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

    def update_stats(self):
        self.totalARM = self.chest.armor_val + self.legs.armor_val + \
            self.shield.armor_val + self.shield.armor_val + self.helmet.armor_val

########
# Weapons
########

class Weapon:

    def __init__(self, name, dmg_l, dmg_h, rng, price):
        self.name = name
        self.dmg_l = dmg_l
        self.dmg_h = dmg_h
        self.rng = rng
        self.price = price

    def give_stats(self):
        print("(" + str(self.dmg_l) + '-' + str(self.dmg_h) + ", range: " + \
            str(self.rng) + ")")


class Sword(Weapon):

    def __init__(self, name, dmg_l, dmg_h, rng, price):
        super().__init__(name, dmg_l, dmg_h, rng, price)
        
    def equip(self, glad):
        if glad.gear.weapon1.name == "None":
            glad.gear.weapon1 = self
        elif glad.gear.weapon2.name == "None":
            glad.gear.weapon2 = self


class Axe(Weapon):
    
    def __init__(self, name, dmg_l, dmg_h, rng, price):
        super().__init__(name, dmg_l, dmg_h, rng, price)
        
    def equip(self, glad):
        if glad.gear.weapon1.name == "None":
            glad.gear.weapon1 = self
        elif glad.gear.weapon2.name == "None":
            glad.gear.weapon2 = self


class Bow(Weapon):

    def __init__(self, name, dmg_l, dmg_h, rng, price):
        super().__init__(name, dmg_l, dmg_h, rng, price)
        
    def equip(self, glad):
        if glad.gear.weapon1.name == "None":
            glad.gear.weapon1 = self
        elif glad.gear.weapon2.name == "None":
            glad.gear.weapon2 = self


class Accesory:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Quiver(Accesory):

    def __init__(self, name, amount, price):
        super().__init__(name, price)
        self.MAX_CAPACITY = amount
        self.amount = amount

    def give_stats(self):
        print("(" + str(self.MAX_CAPACITY) + " capacity)")

    def equip(self, glad):
        glad.gear.weapon_acc = self

########
# Armor
########

class Armor:

    def __init__(self, name, armor_val, price):
        self.name = name
        self.armor_val = armor_val
        self.price = price

    def give_stats(self):
        print("(" + str(self.armor_val) + " armor)")


class Chestplate(Armor):

    def __init__(self, name, armor_val, price):
        super().__init__(name, armor_val, price)

    def equip(self, glad):
        glad.gear.chest = self
        print("chest")
        input()


class Legs(Armor):

    def __init__(self, name, armor_val, price):
        super().__init__(name, armor_val, price)

    def equip(self, glad):
        glad.gear.legs = self
        print("legs")
        input()

class Shield(Armor):

    def __init__(self, name, armor_val, price):
        super().__init__(name, armor_val, price)

    def equip(self, glad):
        glad.gear.shield = self
        print("shield")
        input()


class Helmet(Armor):

    def __init__(self, name, armor_val, price):
        super().__init__(name, armor_val, price)

    def equip(self, glad):
        glad.gear.helmet = self
        print("helmet")
        input()