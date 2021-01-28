from app.models.event import *

event_1 = Event("21/1/2021", "Brexit day", 0, "Parents basement", "Boring as fuck", True)
event_2 = Event("25/12/2020", "Christmas", "max 6 from 2 households", "Everywhere", "It's christmas time!!!", True)

events = [event_1, event_2]

recurring_event_list = []
event_list = []

for event in events:
    if event.recurring:
        recurring_event_list.append(event)
    else:
        event_list.append(event)
