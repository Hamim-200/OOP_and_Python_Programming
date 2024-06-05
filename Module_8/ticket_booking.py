class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        self.__bookings = {}
        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[show_id] = [['0' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self.__seats:
            raise ValueError(f"Show ID {show_id} does not exist.")
        for row, col in seats_to_book:
            if row >= self.__rows or col >= self.__cols or row < 0 or col < 0:
                raise ValueError(f"Seat ({row}, {col}) is invalid.")
            if self.__seats[show_id][row][col] != '0':
                raise ValueError(f"Seat ({row}, {col}) is already booked.")
            self.__seats[show_id][row][col] = '1'
        
        if show_id not in self.__bookings:
            self.__bookings[show_id] = []
        self.__bookings[show_id].extend(seats_to_book)

    def view_show_list(self):
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError(f"Show ID {show_id} does not exist.")
        print(f"Available seats for Show ID {show_id}:")
        for row in self.__seats[show_id]:
            print(' '.join(row))

    def view_booking_details(self):
        print("Your Booking Details:")
        for show_id, seats in self.__bookings.items():
            show_details = next((show for show in self.__show_list if show[0] == show_id), None)
            if show_details:
                print(f"\nShow ID: {show_id}, Movie: {show_details[1]}, Time: {show_details[2]}")
                print("Booked Seats:")
                for row, col in seats:
                    print(f"Seat ({row}, {col})")

print('................................')
print('    MOVIE TICKET SITE!!')
print('................................')

def main():
    hall1 = Hall(5, 5, 'Hall 1')
    hall1.entry_show('S1', 'Jawan', '12:00 PM')
    hall1.entry_show('S2', 'Pathan', '03:00 PM')
    hall1.entry_show('S3', 'Dunky', '06:00 PM')

    while True:
        print("\n1. View all shows")
        print("2. View available seats")
        print("3. Book tickets")
        print("4. View your booking details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for hall in Star_Cinema.get_hall_list():
                print(f"\nHall No: {hall._Hall__hall_no}")
                hall.view_show_list()

        elif choice == '2':
            show_id = input("Enter show ID to view available seats: ")
            for hall in Star_Cinema.get_hall_list():
                try:
                    hall.view_available_seats(show_id)
                except ValueError as e:
                    print(e)

        elif choice == '3':
            show_id = input("Enter show ID to book seats: ")
            try:
                num_seats = int(input("How many seats do you want to book? "))
            except ValueError:
                print("Invalid number. Please enter an valid integer value.")
                continue
            seats_to_book = []
            for i in range(num_seats):
                while True:
                    try:
                        seat = input(f"Enter seat row and column for seat {i + 1} (example., 1 2): ")
                        row, col = map(int, seat.split())
                        seats_to_book.append((row, col))
                        break
                    except ValueError:
                        print("Invalid input. Please enter the seat row and column")

            for hall in Star_Cinema.get_hall_list():
                try:
                    hall.book_seats(show_id, seats_to_book)
                    print("Seats booked successfully!!!!!")
                    break
                except ValueError as e:
                    print(e)

        elif choice == '4':
            for hall in Star_Cinema.get_hall_list():
                hall.view_booking_details()

        elif choice == '5':
            print("Logout...")
            print("Please Run again for login.")
            break

        else:
            print("INVALID. Please try again.")

if __name__ == "__main__":
    main()
