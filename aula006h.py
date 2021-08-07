#Record of a shopping list in a system
#Each product with name, Amount and unitary price
item = []  #Empty list
shopping_list = [] #Oficial shopping list
for i in range(3):
    item.append(input('Type in the item name:'))
    item.append(int(input('Type in the amount of the item:')))
    item.append(float(input('Type in the price:')))
    item.clear() #to populate each item list and clean again to insert a new product(reinsertion)
print(shopping_list)


