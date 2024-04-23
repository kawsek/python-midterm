class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall()

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

    def allocate_seats(self, show_id):
        if show_id not in self.seats:
            seats = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append('O')
                seats.append(row)
            self.seats[show_id] = seats
        return self.seats[show_id]

    def entry_show(self, id, movie_name, time):
        entry = (id,movie_name, time)
        self.show_list.append(entry)
        self.allocate_seats(id)

    def book_seats(self,show_id, seat_list):
        show_ids = []
        for show in self.show_list:
            show_ids.append(show[0])
        if show_id not in show_ids:
            print("INVALID SHOW ID")
            return
    
        seats = self.allocate_seats(show_id)

        for seat in seat_list:
            row,col = seat
            if row < 1 or row > self.rows or col < 1 or col> self.cols:
                print("INVALID SEAT.")
                return
            if seats[row-1][col-1] == 'X':
                print("SEAT ALREADY BOOKED.")
                return
            seats[row - 1][col -1] = 'X'
        print("SEATS BOOKED SUCCESSFULLY.")

    def view_show_list(self):
        print("SHOWS RUNNING IN HALL", self.hall_no)
        print("--------")
        for show in self.show_list:
            # print("---------")
            print("MOVIE NAME:", show[1], "  ID:", show[0], "  TIME:", show[2])
        print("---------")

    def view_available_seats(self, show_id):
        show_ids = []
        for show in self.show_list:
            show_ids.append(show[0])
        if show_id not in show_ids:
            print("INVALID SHOW ID.")
            return 

        seats = self.allocate_seats(show_id)
        print("AVAILABLE SEATS FOR SHOW ID", show_id)

        for i in range(self.rows):
            for j in range(self.cols):
                print(seats[i][j], end = " ")
            print()


hall1 = Hall(5, 10, 1)
hall1.entry_show("333", "bidai prithibi", "14:00 pm")
hall1.entry_show("444", "jibone ki korlam", "15:00 pm")
hall1.book_seats("333", [(1, 2), (3, 4)])

run = True
while run:
    print("1. VIEW ALL SHOW TODAY ")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKETS.")
    print("4. EXIT")

    option = input("ENTER OPTION: ")

    if option == '1':
        for hall in Star_Cinema.hall_list:
            hall.view_show_list()

    elif option == '2':
        show_id = input("ENTER SHOW ID: ")
        for hall in Star_Cinema.hall_list:
            hall.view_available_seats(show_id)

    elif option == '3':
        show_id = input("ENTER SHOW ID: ")
        n = int(input("NUMBER OF TICKET: "))
        while n:
            row = int(input("ENTER ROWS: "))
            col = int(input("ENTER COLS: "))
            out = (row, col)
            seat_list = []
            seat_list.append(out)
            for hall in Star_Cinema.hall_list:
                hall.book_seats(show_id, seat_list)
            n -= 1

    elif option == '4':
        print("THANK YOU FOR USING THIS SYSTEM !")
        run = False