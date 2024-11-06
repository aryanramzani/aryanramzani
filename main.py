class Ticket:

    def __init__(self,ticket_id,description):
        self.ticket_id = ticket_id
        self.description = description

        self.status = "open"

    def Resolve(self):
        self.status = "Resove"


class TicketSystem:

    def __init__(self):
        self.tickets = []
        self.next_id = 1

    def create_ticket(self,description):
        ticket = Ticket(self.next_id, description)

        self.tickets.append(ticket)

        self.next_id += 1

        print(f"Ticket #{ticket.ticket_id}created.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets found")

        else:
            for ticket in self.tickets:
                print(f"ID: {ticket.ticket_id},Description:{ticket.description}, status:{self.status}")

    def resolve_ticket(self,ticket_id):
        for ticket in self.tickets:

            if ticket.ticket_id == ticket_id:

                ticket.resolve()

                print(f"Ticket #{ticket_id}resolved.")
                return
        print(f"Ticket #t{ticket_id}not found.")

def main() :

    system = TicketSystem()

    while True:
        print("\nTicket Managment System")


        print("1. Create Ticket")
        print("2. View Ticket")
        print("3. Resolve Ticket")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1" :
            description = input("Enter The Ticket Description:")

            system.create_ticket(description)

        elif choice == "2" :
            system.view_tickets()
        elif choice == "3" :
            try:
                ticket_id = int(input("Enter the Ticket ID to Resolve:"))

                system.resolve_ticket(ticket_id)
            except ValueError:
                print("Invalid Ticket ID.Please Inter a Number.")

        elif choice == "4":
            print("Exiting the Ticket Managment System.")
            break
        else:
            print("Invalid Choice.Please Select a valid option!")

if __name__ == "__main__":
    main()

