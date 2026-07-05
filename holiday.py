while True:
    city_flight = input("Are you flying to Paris, Florence or Tokyo?").lower()
    if city_flight in ["paris", "florence", "tokyo"]:
        break
    else:
        print("Error - city not recognised. Please try again.")

num_nights = int(input("How many nights are you staying at a hotel?"))

rental_days = int(input("How many days are you hiring a car?"))

def hotel_cost(num_nights):
    total_hotel_cost = num_nights * 85
    return total_hotel_cost

def plane_cost(city_flight):
    if city_flight == "paris":
        cost = 40
    elif city_flight == "florence":
        cost = 95
    elif city_flight == "tokyo":
        cost = 750
    return cost

def car_rental(rental_days):
    total_car_cost = rental_days * 30
    return total_car_cost

def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

print(f"Your total holiday costs £{holiday_cost(num_nights, city_flight, rental_days)}")





