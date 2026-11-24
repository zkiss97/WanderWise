from data_generator import generate_customers
from data_generator import generate_hotels
from data_generator import generate_bookings
from data_export import export_customers_json
from data_export import export_hotels_json
from data_export import export_bookings_json

customer_list = generate_customers(50)
export_customers_json(customer_list)

hotels_data = generate_hotels(50)
export_hotels_json(hotels_data)

booking_list = generate_bookings(50)
export_bookings_json(booking_list)