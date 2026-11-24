from datetime import date

class Customer:
    customer_name = str
    customer_id = str
    date_of_birth = str
    gender = bool
    category = str
    premium = bool

    def __init__(self, customer_name, customer_id, date_of_birth, gender, category, premium):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.category = category
        self.premium = premium

    def __str__(self):
        return f"{self.name} ({self.CustID}, {self.date_of_birth}, {self.gender}, {self.category})"

    @staticmethod
    def calculate_age(date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year
        return age

    @staticmethod
    def calculate_category(age):
        if age <= 1:
            pax = "Infant"
        elif age > 2 and age <= 9:
            pax = "Child"
        elif age > 10 and age <= 17:
            pax = "Teenager"
        elif age > 65:
            pax = "Elder"
        else:
            pax = "Adult"
        return pax


class Hotel:
    hotel_id = str
    hotel_name = str
    city = str
    country = str
    stars = int
    price_per_night = int


    def __init__(self, hotel_id, hotel_name, city, country, stars, price_per_night):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.city = city
        self.country = country
        if not 2 <= stars <= 5:
            raise ValueError("Stars must be between 2 and 5")
        self.stars = stars
        if price_per_night <= 0:
            raise ValueError("Price for night must be greater than 0")
        self.price_per_night = price_per_night

    def __str__(self):
        return f"{self.hotel_id} {self.hotel_name} ({self.city}, {self.stars} stars, {self.price_per_night} euros)"


class Booking:
    booking_id = str
    customer_name = str
    customer_id = str
    hotel_name = str
    hotel_id = str
    check_in_date = date
    checkout_date = date
    number_of_infants = int
    number_of_children = int
    number_of_teenagers = int
    number_of_adults = int
    number_of_elders = int
    total_price = int

    def __init__(self, booking_id, customer, hotel, check_in_date, checkout_date, number_of_infants,
                 number_of_children, number_of_teenagers, number_of_adults, number_of_elders, total_price):
        self.booking_id = booking_id
        self.customer = customer
        self.hotel = hotel
        if check_in_date > checkout_date:
            raise ValueError("Check in date must be before checkout date")
        self.check_in_date = check_in_date
        self.checkout_date = checkout_date
        if number_of_infants < 0:
            raise ValueError("Number of infants must not be less than 0")
        self.number_of_infants = number_of_infants
        if number_of_children < 0:
            raise ValueError("Number of children must not be less than 0")
        self.number_of_children = number_of_children
        if number_of_teenagers < 0:
            raise ValueError("Number of teenagers must not be less than 0")
        self.number_of_teenagers = number_of_teenagers
        if number_of_adults < 0:
            raise ValueError("Number of adults must not be less than 0")
        self.number_of_adults = number_of_adults
        if number_of_elders < 0:
            raise ValueError("Number of elders must not be less than 0")
        self.number_of_elders = number_of_elders
        if number_of_adults + number_of_elders < 1:
            raise ValueError("Every booking must contain at least 1 adult or 1 elder")
        self.total_price = total_price

    @staticmethod
    def price_calculator(check_in_date, checkout_date, number_of_infants, number_of_children,
                         number_of_teenagers, number_of_adults, number_of_elders, stars, price_per_night, premium) -> float:
        nights = (checkout_date - check_in_date).days
        number_of_people = number_of_infants + number_of_children + number_of_teenagers + number_of_adults + number_of_elders
        if stars == 2:
            star_multiplier = 0.9
        elif stars == 4:
            star_multiplier = 1.1
        elif stars == 5:
            star_multiplier = 1.2
        else:
            star_multiplier = 1

        total_price = nights * price_per_night * star_multiplier * (0.5 * number_of_infants + 0.5 * number_of_children +
                                                                    0.7 * number_of_teenagers + number_of_adults + 0.5 * number_of_elders)
        if premium:
            return total_price * 0.9
        else:
            return total_price

    def __str__(self):
        all_people = (self.number_of_infants + self.number_of_children +
                      self.number_of_teenagers + self.number_of_adults +
                      self.number_of_elders)
        return (f"{self.booking_id} | "
                f"{self.customer.customer_name} | "
                f"{self.hotel.hotel_name} | "
                f"{all_people} guests | "
                f"{self.total_price:.2f} euros")



"""B1 = Booking(
    booking_id="B001",
    customer_id="C001",
    hotel_id="H001",
    check_in_date = date(2024, 5, 1),
    checkout_date = date(2024, 5, 2),
    number_of_infants = 0,
    number_of_children = 0,
    number_of_teenagers = 1,
    number_of_adults = 0,
    number_of_elders = 1,)
print(B1.price_calculator(B1.check_in_date, B1.checkout_date,B1.number_of_infants, B1.number_of_children, B1.number_of_teenagers, B1.number_of_adults,
                          B1.number_of_elders, stars = 5, price_per_night = 100, premium = True))

print(B1)"""