import json

def export_customers_json(customer_list):
    customers_data = []

    for customer in customer_list:
        one_customer = {
            "customer_name": customer.customer_name,
            "customer_id": customer.customer_id,
            "date_of_birth": customer.date_of_birth.isoformat(),
            "gender": customer.gender,
            "category": customer.category,
            "premium": customer.premium,
        }
        customers_data.append(one_customer)

    with open('exports/customers_data.json', 'w', encoding='utf-8') as file:
        json.dump(customers_data, file, indent=4)


def export_hotels_json(hotel_list):
    hotels_data = []
    for hotel in hotel_list:

        one_hotel = {
            "hotel_id": hotel.hotel_id,
            "hotel_name": hotel.hotel_name,
            "hotel_city": hotel.city,
            "hotel_country": hotel.country,
            "hotel_stars": hotel.stars,
            "price_per_night": hotel.price_per_night
        }
        hotels_data.append(one_hotel)
    with open("exports/hotels_data.json", "w", encoding="utf-8") as file:
        json.dump(hotels_data, file, indent=4)


def export_bookings_json(bookings_list):
    bookings_data = []

    for booking in bookings_list:
        one_booking = {
            "booking_id": booking.booking_id,
            "customer_id": booking.customer.customer_id,
            "hotel_id": booking.hotel.hotel_id,
            "check_in_date": booking.check_in_date.isoformat(),
            "checkout_date": booking.checkout_date.isoformat(),
            "number_of_infants": booking.number_of_infants,
            "number_of_children": booking.number_of_children,
            "number_of_teenagers": booking.number_of_teenagers,
            "number_of_adults": booking.number_of_adults,
            "number_of_elders": booking.number_of_elders,
            "total_price": booking.total_price
        }
        bookings_data.append(one_booking)

    with open("exports/bookings_data.json", "w", encoding="utf-8") as file:
        json.dump(bookings_data, file, indent=4)