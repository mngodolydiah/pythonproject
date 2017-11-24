class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Events(User):
    def addevent(self, eventname, eventdateandtime, eventlocation, eventticket):
        self.eventname = eventname
        self.eventdateandtime = eventdateandtime
        self.eventlocation = eventlocation
        self.eventticket = eventticket
