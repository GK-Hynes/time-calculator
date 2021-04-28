def add_time(start_time, duration, start_day=None):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    am_pm = ""
    end_hours = 0
    end_mins = 0

    # Get starting hours and minutes
    am_pm = start_time.split(" ")[1]
    start_times = start_time.split(" ")[0]
    start_hours = int(start_times.split(":")[0])
    start_mins = int(start_times.split(":")[1])

    # Get hours and minutes to add
    duration_hours = int(duration.split(":")[0])
    duration_mins = int(duration.split(":")[1])

    num_days_added = duration_hours // 24

    end_mins = start_mins + duration_mins
    if(end_mins >= 60):
        start_hours += 1
        end_mins = end_mins % 60
    am_pm_changes = (start_hours + duration_hours) // 12
    end_hours = (start_hours + duration_hours) % 12

    # Make sure end minutes are formatted
    if(end_mins < 10):
        end_mins = "0" + str(end_mins)

    # Handle hours being 0
    if end_hours == 0:
        end_hours = 12

    if (am_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
        num_days_added += 1

    # Change between am and pm
    if am_pm_changes % 2 == 1 and am_pm == "PM":
        am_pm = "AM"
    elif am_pm_changes % 2 == 1 and am_pm == "AM":
        am_pm = "PM"

    end_time = f"{end_hours}:{end_mins} {am_pm}"
    
    if start_day:
        start_day = start_day.lower()
        lowered_weekdays = []
        for day in weekdays:
            lowered_weekdays.append(day.lower())
        day_index = ((lowered_weekdays.index(start_day)) + num_days_added) % 7
        print(f"Day index: {day_index}")
        new_day = weekdays[day_index]
        end_time = f"{end_time}, {new_day}"
    
    if num_days_added == 1:
        end_time = f"{end_time} (next day)"
    elif num_days_added > 1:
        end_time = f"{end_time} ({num_days_added} days later)"

    print(end_time)


# Sample inputs
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)