from datetime import *

class Event:
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.venues = []  # Plural for list

    def addVenue(self, venue):
        self.venues.append(venue)
    
class Venue:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def addAddress(self, address):
        self.addresses.append(address)
        
class Address:
    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country

# Create instances
e = Event("Kaira's Birthday", date(2021, 9, 2), date(2021, 9, 2))
v = Venue("Abhinay Grand Hotel")
a = Address("Road No-1", "Hyderabad", "Telangana", "India")

# Add address to venue, venue to event
v.addAddress(a)
e.addVenue(v)

# Print the output
print(f"Today's Event: {e.name}")
for venue in e.venues:
    print(f" Venue: {venue.name}")
    for addr in venue.addresses:
        print(f"  Address: {addr.street}, {addr.city}, {addr.state}, {addr.country}")
