
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
def time_index_to_string(index: int) -> str:
    if index < 0 or index > 24 * 4 * 7:
        return "Time index out of range"

    index %=  24 * 4 
    
    hour = index // 4
    quarter = index % 4 * 15

    return str(hour) + ":" + f"{quarter:02d}"


def time_index_to_day(index: int) -> str:
    if index < 0 or index > 24 * 4 * 7:
        return "Time index out of range"

    index //= 24*4

    return WEEK_DAYS[index]


