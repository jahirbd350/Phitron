class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        new_show_list = (id, movie_name, time)
        self.show_list.append(new_show_list)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def book_seats(self, id, seat):
        if id in self.seats:
            for row,col in seat:
                row -=1; col -=1
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(f"Seat {row+1}, {col+1} booked successfully!")
                else:
                    print(f"Seat {row+1}, {col+1} is already booked!")
        else:
            print(f"Wrong Show ID: {id}")
    
    def view_show_list(self):
        if not self.show_list:
            print("\nNo shows available.")
        else:
            for show in self.show_list:
                print(f"Show ID: {show[0]}, Movie Title: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print(f"\nAvailable seats for Show ID {show_id}:")
            for row in self.seats[show_id]:
                print(row)
        else:
            print(f"\nWrong show ID: {show_id} ")

sh = Hall(4,4,22)
sh.entry_show(111, "Jawan", "4PM")
sh.entry_show(112, "Behind Enemy Lines", "7PM")
# sh.view_show_list()
# sh.view_available_seats(111)
# sh.book_seats(111, [(1,1), (2,3)])
# sh.view_available_seats(111)


run = True
while run:
    
    print("\nOptions: ")
    print("1 : View All Shows")
    print("2 : View available seats")    
    print("3 : Book seat")    
    print("4 : Create new show") 
    print("5 : Logout") 

    op = int(input("Enter your option: "))
    if op==1:
        sh.view_show_list()
    elif op == 2:
        id = int(input("Enter show id: "))
        sh.view_available_seats(id)    
    elif op == 3:
        id = int(input("Enter show id: "))
        no_of_seat = int(input("Number of ticket: "))
        st = []
        while no_of_seat>0:
            while True:
                row = int(input("Enter row no: "))
                if(row > sh.rows):
                    print("Row out of bound!")
                    continue
                else:
                    break
            while True:
                col = int(input("Enter col no: "))
                if(col > sh.cols):
                    print("Column out of bound!")
                    continue
                else:
                    break
            st.append((row,col))
            no_of_seat -=1
        sh.book_seats(id,st)
    elif op==4:
        id = int(input("Enter show id: "))
        name = (input("Enter Movie name: "))
        time = (input("Enter show time: "))
        sh.entry_show(id,name,time)
    elif op==5:
        run = False