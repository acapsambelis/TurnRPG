'''
    Creates weapons and armor using classes
    from itemLibrary.py
'''

from itemLibrary import *

# Swords
bareSwd = Sword("None", 0, 0, 1)
bronzeSwd = Sword("Bronze sword", 0, 10, 2)
ironSwd = Sword("Iron sword", 10, 25, 2)
broadSwd = Sword("Broadsword", 25, 40, 2)

swordLst = [bareSwd, broadSwd, ironSwd, broadSwd]

# Axes
bareAxe = Axe("None", 0, 0, 1)
bronzeAxe = Axe("Bronze axe", 0, 15, 3)
steelAxe = Axe("Steel axe", 15, 30, 3)

axeLst = [bareAxe, bronzeAxe, steelAxe]

# Bows
bareBow = Bow("None", 0, 0, 1)
slingshotBow = Bow("Slingshot", 0, 5, 10)
huntingBow = Bow("Hunting Bow", 5, 15, 15)
longBow = Bow("Longbow", 15, 30, 30)

bowLst = [bareBow, slingshotBow, huntingBow, longBow]

# Accessories
emptyQui = Quiver("Empty", 0)
huntingQui = Quiver("Hunting quiver", 5)
trainingQui = Quiver("Training quiver", 10)

quiverLst = [emptyQui, huntingQui, trainingQui]
accessLst = [[None], quiverLst]

# Chestplates
bareCP = Chestplate("None", 0)
leatherCP = Chestplate("Leather breastplate", 25)
chainCP = Chestplate("Chain mail chestplate", 40)

chestLst = [bareCP, leatherCP, chainCP]

# Legs
bareLG = Legs("None", 0)
leatherLG = Legs("Leather pants", 25)
chainLG = Legs("Chain mail pants", 40)

legLst = [bareLG, leatherLG, chainLG]

# Shield
bareSH = Shield("None", 0)
woodSH = Shield("Wooden shield", 25)
ironSH = Shield("Iron shield", 40)

shieldLst = [bareSH, woodSH, ironSH]

# Helmet
bareHM = Helmet("None", 0)
leatherHM = Helmet("Leather cap", 25)
chainHM = Helmet("Chain mail helmet", 40)

helmetLst = [bareHM, leatherHM, chainHM]


item_type_dict = {
    "<class 'itemLibrary.Sword'>": swordLst, \
    "<class 'itemLibrary.Axe'>": axeLst, \
    "<class 'itemLibrary.Bow'>": bowLst, \
    "<class 'itemLibrary.Chestplate'>": chestLst, \
    "<class 'itemLibrary.Legs'>": legLst, \
    "<class 'itemLibrary.Shield'>": shieldLst, \
    "<class 'itemLibrary.Helmet'>": helmetLst, \
    "<class 'itemLibrary.Quiver'>": quiverLst
    }
