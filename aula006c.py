#Listing items inside a tuple using for (with range)
backpack = ('Axe (index 0)', 'Shirt (index 1)', 'Bacon (index 2 )', 'Avocado (index 3)')
size = len(backpack)
for item in range(0, size, 1):
    print('In my back pack I have: {}'.format(backpack[item]))
