
# Days
WEEK_DAYS = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

PRIORITY = {
    -1:"",
    0: "Low",
    1: "Medium",
    2: "High"
}

# Axis 1: Time index 
# Axis 2: Events
# Axis 3: Event array: [user_id, name, priority]
def generate_shedule() -> list:
    TIME_SLOTS = 7 * 24 * 4
    return [[] for i in range(TIME_SLOTS)]


def add_event(schedule: list, start_index: int, end_index: int, user_id: str, name: str, priority: int):
    """Adds event to array"""
    event = [user_id, name, priority]
    for i in range(start_index, end_index):
        schedule[i].append(event)


def find_user_event(schedule: list, user_id: str) -> list:
    """Returns a list of all events of the given user"""
    user_events = []
    for event in schedule:
        if event[0] == user_id:
            user_events.append(event)
    return user_events


# ============================================ CONVERSIONS =================================
# To int
def time_index_to_min(index: int) -> int:
    index %=  24 * 4 
    return index % 4 * 15

def time_index_to_hour(index: int) -> int:
    index %=  24 * 4 
    return index // 4

def time_index_to_day(index: int) -> int:
    return index // (24*4)

# To string
def time_index_to_string(index: int) -> str:
    if index < 0 or index > 24 * 4 * 7:
        return "Time index out of range"

    hour = time_index_to_hour(index)
    quarter = time_index_to_min(index)

    return str(hour) + ":" + f"{quarter:02d}"

def time_index_to_day_string(index: int) -> str:
    if index < 0 or index > 24 * 4 * 7:
        return "Time index out of range"

    return WEEK_DAYS[time_index_to_day(index)]


# To timetable
def schedule_to_event_data(schedule: list) -> list:
    """converts the schedule list into an array of event_data that is readable by the timetable"""

    # Event array (schedule): ["username#id", event_name:str, priority: int(0-3)]
    # Event data (timetable): [Day, Start (hr), Start (min), duration (min), Name] 

    # Axis 1: Unique events
    # Axis 2: [Event array, time]
    current_events_time = [[] for i in range(0)] 

    # Final output
    event_data_list = []

    # TODO: Finish this shit
    for i in range(len(schedule)):
        found_events = []

        for j in range(len(schedule[i])):
            event = schedule[i][j]
            found_events.append(event)

            # On new event added
            if not any(event in events_time for events_time in current_events_time):
                #print("Added", event)
                current_events_time.append([event, 15])
            else:
            # On event exists
                
                for k in range(len(current_events_time)):
                    if current_events_time[k][0] == event:
                        #print("Found", current_events_time[k][0])
                        current_events_time[k][1] += 15
        
        # On event removed (finished); search for events in current_events_time that is not in schedule
        for event_time in current_events_time:
            # If this event has just been added
            if event_time[0] in found_events:
                continue
            else:
                event_data_list.append(schedule_event_to_timesable_event(event_time[0], i, event_time[1]))
                current_events_time.remove(event_time)

    return event_data_list


def schedule_event_to_timesable_event(event: list, end_index: int, duration: int) -> list:
    
    start_time = end_index - duration//15
    start_day = time_index_to_day(start_time)
    start_hour = time_index_to_hour(start_time)
    start_min = time_index_to_min(start_time)

    print("Index:", end_index, "End" )
    print(start_time, start_day)

    username = event[0].rsplit("#", 1)[0] # Ignore second half which is the id
    eventname = event[1]
    priority = event[2]
    event_name = username + ":\n" + eventname + "\n" + PRIORITY[priority]

    return [start_day, start_hour, start_min, duration, event_name]


