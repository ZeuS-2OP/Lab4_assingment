class FlightTableRow:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f'{self.p_id} | {self.process} | {self.start_time} | {self.priority}'


class FlightTable:
    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def sort_table(self, sort_option):
        if sort_option == 1:  # Sort by P_ID
            self.rows.sort(key=lambda row: row.p_id)
        elif sort_option == 2:  # Sort by Start Time
            self.rows.sort(key=lambda row: row.start_time)
        elif sort_option == 3:  # Sort by Priority
            self.rows.sort(key=lambda row: row.priority, reverse=True)
        else:
            print("Invalid sorting option")

    def print_table(self):
        print("P_ID | Process  | Start Time | Priority")
        for row in self.rows:
            print(row)


if __name__ == "__main__":
    flight_table = FlightTable()

    # Add rows to the table
    flight_table.add_row(FlightTableRow("P1  ", "VSCode  ", 100,"        MID"))
    flight_table.add_row(FlightTableRow("P23 ", "Eclipse ", 234,"        MID"))
    flight_table.add_row(FlightTableRow("P93 ", "Chrome  ", 189,"        High"))
    flight_table.add_row(FlightTableRow("P42 ", "JDK     ", 9  ,"          High"))
    flight_table.add_row(FlightTableRow("P9  ", "CMD     ", 7  ,"          High"))
    flight_table.add_row(FlightTableRow("P87 ", "NotePad ", 23 ,"         Low"))

    print("Flight Table (Unsorted):")
    flight_table.print_table()

    sort_option = int(input("\nChoose a sorting parameter: \n1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n"))

    flight_table.sort_table(sort_option)
    print("\nFlight Table (Sorted):")
    flight_table.print_table()
