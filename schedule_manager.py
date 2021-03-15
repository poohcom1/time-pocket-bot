
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

# Axis 1: Time index 
# Axis 2: Events
# Axis 3: Event data: [user_id, priority, name]
def generate_shedule() -> list:
    TIME_SLOTS = 7 * 24 * 4
    return [[[0 for k in range(0)] for j in range(0)] for i in range(TIME_SLOTS)]


def add_event(schedule: list, start_time: int, end_time: int, user_id: str, priority: int, name: str):
    """Adds event to array"""
    event = [user_id, priority, name]
    for i in range(start_time, end_time):
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
    return index // 24*4

def time_index_to_string(index: int) -> str:
    if index < 0 or index > 24 * 4 * 7:
        return "Time index out of range"

    hour = time_index_to_hour(index)
    quarter = time_index_to_min(index)

    return str(hour) + ":" + f"{quarter:02d}"

# To string
def time_index_to_day(index: int) -> str:
    if index < 0 or index > 24 * 4 * 7:
        return "Time index out of range"

    return WEEK_DAYS[time_index_to_day(index)]


def schedule_to_event_data(schedule: list) -> list:
    """converts the schedule list into an array of event_data that is readable by the timetable"""

    # Store events in current index, so find the end time when the event is removed
    current_events = [[] for i in range(0)] # Axis 1: Unique events, Axis 2: event data
    event_data = []

    # TODO: Finish this shit

