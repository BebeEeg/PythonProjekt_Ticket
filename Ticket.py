class Ticket:
    def __init__(self, ticket_id, title, status="Open"):
        self.ticket_id = ticket_id
        self.title = title
        self.status = status
    
    def __str__(self):
        return f"Ticket #{self.ticket_id}: {self.title} ({self.status})"
    
    def close(self):
        self.status = "Closed"
    
    def reopen(self):
        self.status = "Open"


if __name__ == "__main__":
    ticket = Ticket(1, "Fix login bug")
    print(ticket)
    ticket.close()
    print(ticket)