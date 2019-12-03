
# This function calculates and prints out the total hotel costs using the amount of nights and price per night entered
# by the user
def hotel_cost(nights, price_per_night):
    global total_hotel_cost
    total_hotel_cost = nights * price_per_night
    print('The total cost of your stay at the hotel is: R' + str(total_hotel_cost))

# This function returns a plane ticket cost based on the destination
def plane_cost(city):
    global total_plane_cost
    if city == 'p':
        total_plane_cost = 13000
    if city == 'b':
        total_plane_cost = 15000
    if city == 'ny':
        total_plane_cost = 18000
    if city == 'br':
        total_plane_cost = 23000
    else:
        total_plane_cost = 0
    print('The total cost of your plane ticket is: R' + str(total_plane_cost))

# This function calculates and returns the cost of car rental based on a fixed price and the number of days the user
# is planning to rent the car
def car_rental(days):
    global total_car_cost
    car_per_day = 300
    total_car_cost = car_per_day * days
    print('The total cost of your car rental for your trip is: R' + str(total_car_cost))

# This function calculated the total holiday cost using all three functions
def holiday_cost(total_hotel_cost, total_plane_cost, total_car_cost):
    total_holiday_cost = total_hotel_cost + total_plane_cost + total_car_cost
    print('The total cost of your holiday will be: R' + str(total_holiday_cost))

# This allows the user to enter all the required information
print('This tool helps you to calculate the total cost of a holiday trip. Please answer the following questions:')
price_per_night = int(input('What is the price per night of your hotel: R'))
nights = int(input('How many nights will you be staying at the hotel: '))
city = input('Which city would you like to land in? Select one of the following:\n' +
             'p - Paris\n' +
             'b - Berlin\n' +
             'ny - New York\n' +
             'br - Brazil\n')
days = int(input('For how many days will you be renting a car: '))

# All the functions are called
hotel_cost(nights, price_per_night)
plane_cost(city)
car_rental(days)
holiday_cost(total_hotel_cost, total_plane_cost, total_car_cost)



