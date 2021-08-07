#Calculate the final price and hte discount in %
price = float(input('Type in the price of the product (R$):'))
percentage = float(input('Type in the percentage of discout(%):'))
discount = price*(percentage/100)
final = price - discount
print('The product costs R${:.2f} and the percentage of discount is {:.0f}% \n '
      'The discount is R${:.2f} and the final price is R${:.2f}' .format(price, percentage, discount, final))
