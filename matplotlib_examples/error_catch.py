rice = input("Enter the price: ")
try:
    price = float(price)
    print('Price =', price)
except ValueError:
    print('Not a number!')
