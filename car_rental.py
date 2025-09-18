from datetime import datetime
import random

class CarRental:
    def __init__(self, stock=10):
        self.stock = stock

    def display_stock(self):
        print(f"Available cars for rent: {self.stock}")
        return self.stock

    def rent_hourly(self, num_of_cars):
        if num_of_cars <= 0 or num_of_cars > self.stock:
            print("Invalid number of cars. Please enter a positive number within available stock.")
            return None
        else:
            self.stock -= num_of_cars
            rental_time = datetime.now()
            print(f"Rented {num_of_cars} car(s) on hourly basis at {rental_time}.")
            return rental_time

    def rent_daily(self, num_of_cars):
        if num_of_cars <= 0 or num_of_cars > self.stock:
            print("Invalid number of cars. Please enter a positive number within available stock.")
            return None
        else:
            self.stock -= num_of_cars
            rental_time = datetime.now()
            print(f"Rented {num_of_cars} car(s) on daily basis at {rental_time}.")
            return rental_time

    def rent_weekly(self, num_of_cars):
        if num_of_cars <= 0 or num_of_cars > self.stock:
            print("Invalid number of cars. Please enter a positive number within available stock.")
            return None
        else:
            self.stock -= num_of_cars
            rental_time = datetime.now()
            print(f"Rented {num_of_cars} car(s) on weekly basis at {rental_time}.")
            return rental_time

    def return_car(self, request):
        rental_time, rental_basis, num_of_cars = request
        if rental_time and rental_basis and num_of_cars:
            self.stock += num_of_cars
            now = datetime.now()
            rental_period = now - rental_time

            bill = 0
            if rental_basis == 'hourly':
                # bill = round(rental_period.total_seconds() / 3600) * 5 * num_of_cars
                bill = random.randint(400, 2000)
            elif rental_basis == 'daily':
                bill = round(rental_period.days) * 20 * num_of_cars
            elif rental_basis == 'weekly':
                bill = round(rental_period.days / 7) * 60 * num_of_cars

            print(f"Thank you for returning {num_of_cars} car(s). Your bill is ${bill}.")
            return bill
        else:
            print("Incomplete return information.")
            return None

class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = None
        self.rental_time = None

    def request_car(self):
        cars = int(input("How many cars would you like to rent? "))
        self.cars = cars
        return self.cars

    def return_car(self):
        if self.rental_time and self.rental_basis and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0

