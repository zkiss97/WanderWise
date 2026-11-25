from data_generator import generate_customers, generate_hotels, generate_bookings
from data_export import export_customers_json, export_hotels_json, export_bookings_json
from data_read import import_hotels_json, import_customers_json, import_bookings_json
from data_export import export_customers_csv, export_hotels_csv, export_bookings_csv
from data_export import export_xlsx
from data_read import  import_xlsx
from data_read import import_customers_csv, import_hotels_csv, import_bookings_csv

customer_list = generate_customers(50)
export_customers_json(customer_list)

hotels_data = generate_hotels(50)
export_hotels_json(hotels_data)

booking_list = generate_bookings(50)
export_bookings_json(booking_list)

imported_customers = import_customers_json()

print(imported_customers[0])
print(type(imported_customers[0]))
print(type(imported_customers[0].date_of_birth))

imported_hotels = import_hotels_json()

print(imported_hotels)
print(type(imported_hotels[0]))

imported_bookings = import_bookings_json(imported_customers, imported_hotels)
print(imported_bookings[0])
print(type(imported_bookings[0]))
print(type(imported_bookings[0].customer))
print(type(imported_bookings[0].hotel))

export_customers_csv(customer_list)

export_hotels_csv(hotels_data)

export_bookings_csv(booking_list)

export_xlsx(customer_list, hotels_data, booking_list)

imported_customers, imported_hotels, imported_bookings = import_xlsx()
print(imported_bookings[0])
print(type(imported_bookings[0].customer))
print(type(imported_bookings[0].hotel))

imported_customers = import_customers_csv()
imported_hotels = import_hotels_csv()
imported_bookings = import_bookings_csv(imported_customers, imported_hotels)

print(imported_bookings[0])
print(type(imported_bookings[0].customer))
print(type(imported_bookings[0].hotel))

print(imported_bookings[0])
print(type(imported_bookings[0]))
print(type(imported_bookings[0].customer))
print(type(imported_bookings[0].hotel))