from car_rental import CarRental, Customer

def main():
    car_rental = CarRental(10)
    customer = Customer()

    while True:
        print("""
        ====== Car Rental Shop =======
        1. Display available cars
        2. Request a car on hourly basis ($5/hour)
        3. Request a car on daily basis ($20/day)
        4. Request a car on weekly basis ($60/week)
        5. Return a car
        6. Exit
        """)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            car_rental.display_stock()

        elif choice == 2:
            customer.rental_basis = 'hourly'
            customer.rental_time = car_rental.rent_hourly(customer.request_car())

        elif choice == 3:
            customer.rental_basis = 'daily'
            customer.rental_time = car_rental.rent_daily(customer.request_car())

        elif choice == 4:
            customer.rental_basis = 'weekly'
            customer.rental_time = car_rental.rent_weekly(customer.request_car())

        elif choice == 5:
            request = customer.return_car()
            car_rental.return_car(request)
            customer.rental_basis, customer.rental_time, customer.cars = None, None, 0

        elif choice == 6:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        print("Thank you for choosing our services")

if __name__ == "__main__":
    main()





