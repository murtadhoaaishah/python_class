import csv
import os
from datetime import datetime

tables = [
    {'number': 1, 'seats': 2},
    {'number': 2, 'seats': 6},
    {'number': 3, 'seats': 2},
    {'number': 4, 'seats': 4},
    {'number': 5, 'seats': 8},
]

class Reservation:

    __reservations_database = './reservations_database.csv'

    def __init__(self, name, party_size, contact, date, time):
        self.name = name
        self.party_size = party_size
        self.contact = contact
        self.date = date
        self.time = time


    def make_reservation(self):
        for table in tables:
            if table['seats'] >= self.party_size and table['number'] not in [table['table_number'] for table in Reservation.__reservations_database]: # loops through the tables list to see if the available seats specified in the tables that can accomodate the perty size and table number does not readily exist in reservations_list list
                reservation_det = {
                    "name": self.name,
                    "party_size": self.party_size,
                    "contact": self.contact,
                    "table_number": table['number'],
                    "date" : self.date,
                    "time" : self.time
                    } #details required to save reservation to the rserved list
                reservation_det['table_number'] = table['number'] #it should add  a key called table_number and set it the table number that suits the party size to it

            new_row = [self.name, self.contact, table['number'], self.party_size, self.date, self.time]
            header = ['name', 'contact', 'table_number', 'party size', 'date', 'time']
            try:
                file_exists = os.path.isfile(Reservation.reservations_database)
                with open(Reservation.__reservations_database, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if not file_exists:
                        writer.writerow(header)
                    writer.writerow(new_row)
                Reservation.__reservations_database.append(reservation_det)
                print(f"table number {table['number']} has been reserved for {self.name} for {self.date} and {self.time}")
            except Exception as e:
                 print(f"Error saving reservation: {e}")
        
        print("No available table for the given party size")

   

    @classmethod
    def view_reservations(cls):
        reserved_table = [reservation['table_number'] for reservation in cls.__reservations_database] #it should loop through the reservations_list list, create a list of all table numbers reserved and save it in reserved table
        print(f"{'Table number' if len(reserved_table) < 2 else 'Table numbers'}available are: {reserved_table}")

    @classmethod
    def cancel_reservation(cls, name, table_number):
        # if name and table_number:
            for reservation in cls.__reservations_database:
                if reservation['name'] == name and reservation['table_number'] == table_number: # it should check if the name and number cancelling the reservation exists on the reservations_list
                    cls.__reservations_database.remove(reservation) #if it does, it should remove it from the list
                    print(f'reservation made for {name} has been cancelled')
                    return
            print(f'no existing reservation made by {name}')

    


    @classmethod
    def modify_reservation(cls, name, table_number, new_party_size):
        for reservation in cls.__reservations_database:
            if reservation['name'] == name and reservation['table_number'] == table_number:
                for table in tables: 
                    if table['seats'] >= new_party_size and table['number'] not in [reservation['table_number'] for reservation in cls.reservations_list]:
                        reservation['party_size'] = new_party_size
                        reservation['table_number'] = table['number']
                        print(f"Reservation for {name} has been changed from table number {table_number} to table number {reservation['table_number']}")
                        return
                print('no table available')
                return

        print(f'no reservation made with the name {name}')

    def check_date(self):
        try:
            return datetime.strptime(self.time, '%y-%m-%d')
        except ValueError:
            print("input a valid date in format YYYY-MM-DD")
            return None




def menu():
    while True:
        print("\n1. Make Reservation\n2. View Reservations\n3. Cancel Reservation\n4. Modify Reservation\n5. Exit")
        menu = input("Enter your choice: ")

        if menu == '1':
            name= input('Enter your name: ')
            party_size = int(input('Enter your party size: '))
            contact_number = int(input('Enter your contact number: '))

            reservation_date = None
            while reservation_date is None:
                date = int(input('Enter reservation date YYYY-MM-DD:'))
                reservation_date = Reservation.check_date(date)
                

           
            time = input('Enter time')

            reservation = Reservation(name, party_size, contact_number, date, time)
            reservation.make_reservation()

        elif menu == '2':
            Reservation.view_reservations()

        elif menu == '3':
            name = input('Enter your name: ')
            table_number = int(input('Enter your table number: '))

            Reservation.cancel_reservation(name, table_number)    

        elif menu == '4':
            name = input('Enter your name: ')
            table_number = int(input('Enter your table number: '))
            new_party_size = int(input('Enter your new party size: '))

            Reservation.modify_reservation(name, table_number, new_party_size)

        elif  menu == '5':
            break

        else:
            print('Choose a valid option on the menu list')

menu()
