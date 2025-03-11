print("\nCafe Menu:")

# Define a list of strings
food_list = ['Bacon', 'Avocado', 'French Fries', 'Diet Pepsi']

for food in food_list:
    print(food)

# Define stock dictionary using food list as keys and stock levels as values
stock_dict = {
    food_list[0]: 24,  # Bacon stock level
    food_list[1]: 10,  # Avocado stock level
    food_list[2]: 50,  # French Fries stock level
    food_list[3]: 100,  # Diet Pepsi stock level
}

print("\nStock:")
for key, value in stock_dict.items():
    print(key, value)

# Define price using the food list as keys and prices as values
price_dict = {
    food_list[0]: 15.50,  # Bacon price
    food_list[1]: 7.00,  # Avocado price
    food_list[2]: 10.00,  # French Fries price
    food_list[3]: 5.50,  # Diet Pepsi price
}

print("\nPrice:")
for key, value in price_dict.items():
    print(key, value)

# Calculate the total stock of items in the cafe using a loop
total_stock = 0  # Initialize the total stock

for food in food_list:
    # Check if the food item exists in the dictionaries to avoid KeyError
    if food in stock_dict and food in price_dict:
        Item_value = stock_dict[food] * price_dict[food]
        total_stock += Item_value


print("\nTotal value of items in stock in rands:", total_stock)
