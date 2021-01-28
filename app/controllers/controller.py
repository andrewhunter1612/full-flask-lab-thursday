from app.models.event_list import event_list, recurring_event_list
from flask import render_template, request, redirect
from app import app
from app.models.event import Event



@app.route('/')
def index():
    return render_template('events.html', title="Event List", events=event_list, recurring_events=recurring_event_list)

@app.route('/', methods=["POST"])
def add_event():
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    event_location = request.form['location']
    event_guest_number = request.form['number']
    event_description = request.form['description']
    recurring_event = True if 'recurring_event' in request.form else False


    new_event = Event(event_date, event_name, event_guest_number, event_location, event_description, recurring_event)

    if recurring_event:
        recurring_event_list.append(new_event)
    else:
        event_list.append(new_event)

    return redirect('/')

@app.route('/<index>', methods=["POST"])
def remove_event(index):
    event_list.remove(event_list[int(index)])
    return redirect('/')
    
