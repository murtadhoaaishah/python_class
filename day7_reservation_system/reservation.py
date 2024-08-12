import csv



tables =[
    {
    'number': 1, 'seats': 2
},
{
    'number': 2, 'seats': 6
},
{
    'number': 3, 'seats': 2
},
{
    'number': 4, 'seats': 4
},
{
    'number': 5, 'seats': 8
}
]

# reservations = {}

def viewTables(tables):
    for table in tables:
        print(table)
# viewTables(tables)

reservations_file = 'reservations_file.csv'

# def make_reservation(tables, reservations):
def make_reservation(tables, assignment_reservations_file):
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    party_size = int(input("Enter the number of people: "))
    date = input("Enter reservation date (YYYY - MM - DD): ")
    time = input("Enter your time: ")

    available_table = [table for table in tables if table['seats'] >= party_size and table['number'] not in reservations_file] 
   

    if not available_table:
        print("table not available for your party size")

    print("Available tables: ")
    for table in available_table:
        print(f"Table {table['number']} - seats: {table['seats']}")

 #table to reserve from available list
    table_number = int(input('Enter table number to reserve: '))

    if table_number not in [table['number'] for table in available_table]:
        print("invalid table number")
        return
    
    new_row= [name,contact, table_number, party_size, date, time]
    header = ['table_number', 'name', 'contact', 'party_size', 'date', 'time']
    try:
        with open(assignment_reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow("Name", "Contact", "Party size", "Table Number", )
            writer.writerow(new_row)
        print(f"Table {table_number} reserved successfully for {name}")

    except Exception as e:
        print(f"error saving reservation: {e}")

make_reservation(tables, reservations_file)

    

    # prompt the user to enter the table number they want to reserve
    # table_number = int(input("Enter table number to reserve: "))

    

    

    # create a new header if header is not present
#     header = ['table_number', 'name', 'contact', 'party_size', 'date', 'start_time', 'end_time']
#     try:
#         file_exists = os.path.exists(reservation_file) and os.path.getsize(reservation_file) > 0
#         # open the reservations file in append mode
#         with open(reservation_file, 'a', newline='') as file:
#             writer = csv.writer(file) #Create a CSV writer object
#             # create/write header if not present
#             if not file_exists:
#                 writer.writerow(header)
#                 writer.writerow(new_row) #Write the new reservation to the file
#             else:
#                 writer.writerow(new_row)

#         # Print a success message
#         print(f"Table {table_number} reserved successfully for {name} on {date} from {start_time} to {end_time}.")
#     except Exception as e:
#         # Print an error message if something goes wrong
#         print(f"Error making reservation: {e}")
#         pass

# def cancel_reservation(reservations_file):
#     name = input("Enter your name: ")
#     reserved_date = input("Enter the date of reservation: ")

#     try:
#         with open(reservations_file, 'r') as file:
#             reader = csv.reader(file)
#             reservations = list(reader)

#         current_reservations = [row for row in reservations if not (row[1] == name and row[4] == reserved_date)]
#         with open(reservations_file, 'w', newline='') as file:
#              writer = csv.writer(file)
#              writer.writerows(current_reservations)
#         if len(current_reservations) == len(reservations):
#             print("No matching reservation found.")
#         else:
#             print(f"Reservation for {name} on {reserved_date} has been cancelled.")
#             pass
#     except Exception as e:
#         print(f"Error canceling reservation: {e}")
#         pass
#Function to view reservations
# def view_reservations(reservations_file):
#     try:
#         with open(reservations_file, 'r') as file:
#             reader = csv.reader(file)
#             reservations = list(reader)
#             print(reservations)
#             # reservations = []
#             if reservations:
#                 reserved_tables = [reservation for reservation in reservations if reservation[reservations]]
#                 print(reserved_tables)
#             if not reservations:
#                 print("No reservations found.")
#             pass
#             # for reservation in reservations:
                
#     except Exception as e:
#         print(f"Error reading reservations: {e}")
#         pass

# def modify_reservation():
    
# def display():
#     # Reservations = reservations_file

#     while True:
#         print("Reservation System")
#         print("1. Make reservation")
#         print("2. View reservation")
#         print("3. Cancel reservation")
#         print("4. Exit")
                
#         choice = input("select: ")

#         if choice == "1":
#             make_reservation(tables, reservations_file)
#         # elif choice == "2":
#         #     view_reservations(reservations_file)

#         # elif choice == "3":
#         #     cancel_reservation(reservations_file)
#         elif choice == "4":
#             break 
#         else:
#             print("Invalid choice")

# display()

        

# make_reservation(tables, reservations_file='reservation.csv')