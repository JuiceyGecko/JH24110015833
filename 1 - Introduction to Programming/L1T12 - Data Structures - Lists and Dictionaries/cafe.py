print("\nCafe Menu:")

# Define a list of strings
food_list = ['Bacon', 'Avocado', 'French Fries', 'Diet Pepsi']

for food in food_list:
    print(food)

# Define stock dictionary with food items as keys and quantities as values
stock_dict = {
    'Bacon': 24,
    'Avocados': 18,
    'French Fries': 10,
    'Diet Pepsi': 50
}

print("\nStock:")
for key, value in stock_dict.items():
    print(key, value)

# Define price dictionary with food items as keys and prices as values
price_dict = {
    'Bacon': 40,
    'Avocados': 25,
    'French Fries': 50,
    'Diet Pepsi': 8
}

print("\nPrice:")
for key, value in price_dict.items():
    print(key, value)

# Calculate the total value of items in stock
item_value = (
    stock_dict['Bacon'] * price_dict['Bacon'] +
    stock_dict['Avocados'] * price_dict['Avocados'] +
    stock_dict['French Fries'] * price_dict['French Fries'] +
    stock_dict['Diet Pepsi'] * price_dict['Diet Pepsi']
)
print("\nTotal value of items in stock in rands:", item_value)
