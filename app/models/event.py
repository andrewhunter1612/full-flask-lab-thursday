class Event():
    def __init__(self, date, event_name, number_of_guests, room_location, description, recurring):
        self.date = date 
        self.event_name = event_name
        self.number_of_guests = number_of_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
