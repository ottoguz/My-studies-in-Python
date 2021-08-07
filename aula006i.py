#Record of a shopping list in a system
#Each product with name, Amount and unitary price
#Simplified version
shopping_list = []
for i in range(3):
    nome = input('Type in the item name:')
    qtd = int(input('Type in the amount of the item:'))
    valor = float(input('Type in the price:'))
    shopping_list.append([nome, qtd, valor])
print(shopping_list)
