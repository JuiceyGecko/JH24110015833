# Function to get the cost of a plane ticket

def get_plane_ticket_cost(city):
    """ The function below calculates the cost
    of a plane ticket to a certain  city.

    city: The name of the city you want to visit.
    returns: The cost of the plane ticket to that city.
    """
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

# Function to get the cost of hiring a car


def get_car_hire_cost(rental_days):
    """ This function will calculate the cost of
    hiring a care for the spefic number of days the user needs.
    """
    return rental_days * 400


# Function to calculate the total cost of the holiday

def holiday_cost(hotel_cost, plane_cost, car_rental):
    """ This function will calculate the total cost of the holiday
    by adding the cost of the hotel, plane ticket and car hire.
    """
    return hotel_cost + plane_cost + car_rental

# Create a dictionary of cities and their costs


cities = {
    'Johannesburg': 1500,
    'Cape Town': 2000,
    'Durban': 2500,
    'Port Elizabeth': 2800,
    'Bloemfontein': 3000,
}

cities = {
    'Johannesburg': 1500,
    'Cape Town': 2000,
    'Durban': 2500,
    'Port Elizabeth': 2800,
    'Bloemfontein': 3000,
}

city = input('Which city are you planning to visit? ').title()

if city in cities:
    print(f'The cost of visiting {city} is R{cities[city]}')
else:
    print('The city you entered is not in the list')

num_nights = int(input('How many nights will you be staying? '))
rental_days = int(input('How many days will you need a hired car? '))

hotel_rate_per_night = 100
hotel_cost = num_nights * hotel_rate_per_night
print(f'The cost of the hotel for {num_nights} nights is R{hotel_cost}')

plane_cost = get_plane_ticket_cost(city)
print(f'The cost of the plane ticket to {city} is R{plane_cost}')

car_rental = get_car_hire_cost(rental_days)
print(f'The cost of hiring a car for {rental_days} days is R{car_rental}')

total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)
print(f'The total cost of the holiday is R{total_cost}')
