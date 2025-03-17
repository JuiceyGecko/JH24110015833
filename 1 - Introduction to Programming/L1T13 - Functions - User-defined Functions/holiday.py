# Create a dictionary of cities and their costs

cities = {
    'Johannesburg': 1500,
    'Cape Town': 2000,
    'Durban': 2500,
    'Port Elizabeth': 2800,
    'Bloemfontein': 3000,
}

# Ask user what city they want to visit
city = input('Which city are you planning to visit? ')
# Check if the city is in the dictionary (Error Handling)
if city in cities:
    print(f'The cost of visiting {city} is R{cities[city]}')
else:
    print('The city you entered is not in the list')

# Ask the user how many nights they will be staying
num_nights = int(input('How many nights will you be staying? '))

# Ask the user how many days they will need a hired car
rental_days = int(input('How many days will you need a hired car?'))

# Define the hotel rate per night
hotel_rate_per_night = 100  # R100 per night

# Calculate the cost of the hotel
hotel_cost = num_nights * hotel_rate_per_night

# Display the cost of the hotel in Rands
print(f'The cost of the hotel for {num_nights} nights is R{hotel_cost}')

# Calculate the cost of the plane ticket

# Function to get the cost of a plane ticket


def get_plane_ticket_cost(city):
    if city == 'Johannesburg':
        return 1500
    elif city == 'Cape Town':
        return 2000
    elif city == 'Durban':
        return 2500
    elif city == 'Port Elizabeth':
        return 2800
    elif city == 'Bloemfontein':
        return 3000
    else:
        return 0


# Get the cost of the plane ticket

plane_cost = get_plane_ticket_cost(city)
print(f'The cost of the plane ticket to {city} is R{plane_cost}')

# Define the cost of hiring a car per day
car_hire_rate_per_day = 400  # R400 per day

# Function to calculate the cost of hiring a car


def get_car_hire_cost(rental_days):
    return rental_days * car_hire_rate_per_day

# Calculate the cost of hiring a car


car_rental = get_car_hire_cost(rental_days)
print(f'The cost of hiring a car for {rental_days} days is R{car_rental}')

# Calculate the total cost of the holiday
total_cost = hotel_cost + plane_cost + car_rental
print(f'The total cost of the holiday is R{total_cost}')
