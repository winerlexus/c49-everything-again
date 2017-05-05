inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket']=['seashell', 'strange berry' ,'lint']
a=inventory['backpack']
sorted(a)
    ##print(sorted(a)) 
a.remove('dagger')
    ##print(inventory)
inventory['gold']+=50
    ##print(inventory['gold'])

