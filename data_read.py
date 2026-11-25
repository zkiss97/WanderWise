import json
from datetime import date
from classes import Customer, Hotel, Booking
from openpyxl import load_workbook
import csv


def import_customers_json():
    with open('exports/customers_data.json') as file:
        customers_data = json.load(file)

    customers = []

    for customer in customers_data:
        one_customer = Customer(
            customer['customer_name'],
            customer['customer_id'],
            date.fromisoformat(customer['date_of_birth']),
            customer['gender'],
            customer['category'],
            customer['premium']
        )
        customers.append(one_customer)
    return customers


def import_hotels_json():
    with open('exports/hotels_data.json', 'r', encoding='utf-8') as file:
        hotels_data = json.load(file)

    hotels = []

    for hotel in hotels_data:
        one_hotel = Hotel(
            hotel['hotel_id'],
            hotel['hotel_name'],
            hotel['hotel_city'],
            hotel['hotel_country'],
            hotel['hotel_stars'],
            hotel['price_per_night']
        )
        hotels.append(one_hotel)
    return hotels

def import_bookings_json(customer_list, hotel_list):
    with open('exports/bookings_data.json', 'r', encoding='utf-8') as file:
        bookings_data = json.load(file)

    bookings = []
    customer_by_id = {customer.customer_id: customer for customer in customer_list}
    hotel_by_id = {hotel.hotel_id: hotel for hotel in hotel_list}

    for booking in bookings_data:
        one_booking = Booking(
            booking['booking_id'],
            customer_by_id[booking['customer_id']],
            hotel_by_id[booking['hotel_id']],
            date.fromisoformat(booking['check_in_date']),
            date.fromisoformat(booking['checkout_date']),
            booking['number_of_infants'],
            booking['number_of_children'],
            booking['number_of_teenagers'],
            booking['number_of_adults'],
            booking['number_of_elders'],
            booking['total_price']
        )
        bookings.append(one_booking)
    return bookings

def import_xlsx():
    workbook = load_workbook('exports/wanderwise_data.xlsx')
    customer_sheet = workbook["Customers"]
    customer_data = list(customer_sheet.values)
    customers = []
    for row in customer_data[1:]:
        one_customer = Customer(
            row[0],
            row[1],
            date.fromisoformat(row[2]),
            row[3],
            row[4],
            row[5]
        )
        customers.append(one_customer)

    hotel_sheet = workbook["Hotels"]
    hotel_data = list(hotel_sheet.values)
    hotels = []

    for row in hotel_data[1:]:
        one_hotel = Hotel(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )
        hotels.append(one_hotel)

    booking_sheet = workbook["Bookings"]
    booking_data = list(booking_sheet.values)
    bookings = []

    customer_by_id = {customer.customer_id: customer for customer in customers}
    hotel_by_id = {hotel.hotel_id: hotel for hotel in hotels}

    for row in booking_data[1:]:
        one_booking = Booking(
            row[0],
            customer_by_id[row[1]],
            hotel_by_id[row[2]],
            date.fromisoformat(row[3]),
            date.fromisoformat(row[4]),
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10]
        )
        bookings.append(one_booking)

    return customers, hotels, bookings

def import_customers_csv():
    with open("exports/customers_data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        customers = []

        for row in reader:
            one_customer = Customer(
                row["customer_name"],
                row["customer_id"],
                date.fromisoformat(row["date_of_birth"]),
                row["gender"] == "True",
                row["category"],
                row["premium"] == "True"
            )
            customers.append(one_customer)

    return customers

def import_hotels_csv():
    with open("exports/hotels_data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        hotels = []

        for row in reader:
            one_hotel = Hotel(
                row["hotel_id"],
                row["hotel_name"],
                row["hotel_city"],
                row["hotel_country"],
                int(row["hotel_stars"]),
                float(row["price_per_night"])
            )
            hotels.append(one_hotel)

    return hotels

def import_bookings_csv(customer_list, hotel_list):
    with open("exports/bookings_data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        bookings = []

        customer_by_id = {customer.customer_id: customer for customer in customer_list}
        hotel_by_id = {hotel.hotel_id: hotel for hotel in hotel_list}

        for row in reader:
            one_booking = Booking(
                row["booking_id"],
                customer_by_id[row["customer_id"]],
                hotel_by_id[row["hotel_id"]],
                date.fromisoformat(row["check_in_date"]),
                date.fromisoformat(row["checkout_date"]),
                int(row["number_of_infants"]),
                int(row["number_of_children"]),
                int(row["number_of_teenagers"]),
                int(row["number_of_adults"]),
                int(row["number_of_elders"]),
                float(row["total_price"])
            )
            bookings.append(one_booking)

    return bookings