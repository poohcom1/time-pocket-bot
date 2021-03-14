# Schedule array
TIME_SLOTS = 7 * 24 * 4

# Axis 1: Time slots, # Axis 2: Event_id (username), # Axis 3: Event meta data
master_schedule = [[[0 for k in range(0)] for j in range(0)] for i in range(TIME_SLOTS)]


def add_event(schedule: list, start_time: int, end_time: int, user_id: str, priority: int, name: str):
    """
    Adds event to array
    """
    event = [user_id, priority, name]
    for i in range(start_time, end_time):
        schedule[i].append(event)


def find_user_event(schedule: list, user_id: str) -> list:
    """
    Returns a list of all events of the given user
    :param schedule:
    :param user_id:
    :return:
    """
    user_events = []
    for event in schedule:
        if event[0] == user_id:
            user_events.append(event)
    return user_events


def timeslot_to_time(timeslot: int) -> [int, int]:
    hour_quadrant = timeslot % 24*4
    minute_quadrant = timeslot % 4
    return hour_quadrant, minute_quadrant
