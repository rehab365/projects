def calculate_price(price, discount=0.1):
"""
Calculate a discounted price.
price: the original price
discount: fraction to subtract (default 10%)
Returns: the final price after discount
"""
return price - (price * discount)
print(calculate_price.__doc__)
help(calculate_price)