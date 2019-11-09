'''
    Creates weapons and armor using classes
    from itemLibrary.py
'''

from itemLibrary import *

# Swords
bareSwd = Sword("None", 0, 0, 1, 0)
bronzeSwd = Sword("Bronze sword", 0, 10, 2, 10)
ironSwd = Sword("Iron sword", 10, 25, 2, 10)
broadSwd = Sword("Broadsword", 25, 40, 2, 10)

swordLst = [bareSwd, bronzeSwd, ironSwd, broadSwd]

# Axes
bareAxe = Axe("None", 0, 0, 1, 0)
bronzeAxe = Axe("Bronze axe", 0, 15, 3, 10)
steelAxe = Axe("Steel axe", 15, 30, 3, 10)

axeLst = [bareAxe, bronzeAxe, steelAxe]

# Bows
bareBow = Bow("None", 0, 0, 1, 0)
slingshotBow = Bow("Slingshot", 0, 5, 10, 10)
huntingBow = Bow("Hunting Bow", 5, 15, 15, 10)
longBow = Bow("Longbow", 15, 30, 30, 10)

bowLst = [bareBow, slingshotBow, huntingBow, longBow]

# Accessories
emptyQui = Quiver("None", 0, 0)
huntingQui = Quiver("Hunting quiver", 5, 10)
trainingQui = Quiver("Training quiver", 10, 10)

quiverLst = [emptyQui, huntingQui, trainingQui]
accessLst = [[None], quiverLst]

# Chestplates
bareCP = Chestplate("None", 0, 0)
leatherCP = Chestplate("Leather breastplate", 25, 10)
chainCP = Chestplate("Chain mail chestplate", 40, 10)

chestLst = [bareCP, leatherCP, chainCP]

# Legs
bareLG = Legs("None", 0, 0)
leatherLG = Legs("Leather pants", 25, 10)
chainLG = Legs("Chain mail pants", 40, 10)

legLst = [bareLG, leatherLG, chainLG]

# Shield
bareSH = Shield("None", 0, 0)
woodSH = Shield("Wooden shield", 25, 10)
ironSH = Shield("Iron shield", 40, 10)

shieldLst = [bareSH, woodSH, ironSH]

# Helmet
bareHM = Helmet("None", 0, 0)
leatherHM = Helmet("Leather cap", 25, 10)
chainHM = Helmet("Chain mail helmet", 40, 10)

helmetLst = [bareHM, leatherHM, chainHM]
