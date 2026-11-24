from faker import Faker
from classes import Customer
from classes import Hotel
from classes import Booking
import datetime
from random import randint, choice

fake = Faker()
#print(fake.name())
#print(fake.date_of_birth(minimum_age=1, maximum_age=90))
#print(fake.boolean())

number_of_customers = 30
number_of_hotels = 10
number_of_bookings = 50

def generate_customers(number_of_customers):
    customers = []
    for i in range(number_of_customers):
        name = fake.name()
        customer_id = f"C{i+1:03d}"
        dob = fake.date_of_birth(minimum_age=1, maximum_age=99)
        age = Customer.calculate_age(dob)
        gender = fake.boolean()
        category = Customer.calculate_category(age)
        premium = fake.boolean()
        one_customer = Customer(name, customer_id, dob, gender, category, premium)
        customers.append(one_customer)
    return customers

def generate_hotels(number_of_hotels):
    hotels = []
    for i in range(number_of_hotels):
        name = f"{fake.last_name()} {choice(["Hotel", "Resort", "Suites", "Inn", "Lodge"])}"
        hotel_id = f"H{i+1:03d}"
        city = fake.city()
        country = fake.country()
        stars = randint(2, 5)
        price_per_night = randint(50, 500)
        one_hotel = Hotel(hotel_id, name, city, country, stars, price_per_night)
        hotels.append(one_hotel)
    hot_cal = randint(1, 100)
    california = Hotel("H001", "Hotel California", "Palm Springs", "US", 5, 666)
    if hot_cal % 2 == 0:
        hotels[0] = california
    return hotels

customer_list = generate_customers(number_of_customers)
hotel_list = generate_hotels(number_of_hotels)

def generate_bookings(number_of_bookings):
    bookings = []
    for i in range(number_of_bookings):
        booking_id = f"B{i+1:03d}"
        customer = choice(customer_list)
        hotel = choice(hotel_list)
        check_in_date = fake.date_between(start_date="today", end_date="+365d")
        checkout_date = check_in_date + datetime.timedelta(days=randint(2, 14))
        number_of_infants = randint(0, 2)
        number_of_children = randint(0, 3)
        number_of_teenagers = randint(0, 3)
        number_of_adults = randint(0, 4)
        number_of_elders = randint(0, 2)
        if number_of_adults + number_of_elders == 0:
            number_of_adults = 1
        stars = hotel.stars
        price_per_night = hotel.price_per_night
        premium = customer.premium
        total_price = Booking.price_calculator(check_in_date, checkout_date,
                                               number_of_infants, number_of_children, number_of_teenagers,
                                               number_of_adults, number_of_elders,
                                               stars, price_per_night, premium)
        one_booking = Booking(booking_id,
                              customer,
                              hotel,
                              check_in_date,
                              checkout_date,
                              number_of_infants,
                              number_of_children,
                              number_of_teenagers,
                              number_of_adults,
                              number_of_elders,
                              total_price)
        bookings.append(one_booking)
    return bookings

booking_list = generate_bookings(number_of_bookings)
for booking in booking_list:
    print(booking)



#customer_list = generate_customers(number_of_customers)
#for customers in customer_list:
    #print(customers)

#hotel_list = generate_hotels(number_of_hotels)
#for hotel in hotel_list:
    #print(hotel)