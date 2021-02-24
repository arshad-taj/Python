'''
Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems) , where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot .
'''

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
def addToInventory(inventory={},itemList=[]):
    for i in itemList:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i]+1
    return inventory

def displayInventory(inventory={}):
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print(f"Totla Number of items : {total_items}")

displayInventory(addToInventory(inventory=inv,itemList=dragonLoot))
