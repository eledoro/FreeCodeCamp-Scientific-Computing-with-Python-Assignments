def add_time(start, duration, weekday=''):
    # start  -  in the 12-hour clock format (ending in AM or PM), string, e.g "11:30 AM"
    # duration  -  number of hours and minutes, string, e.g. "2:32"
    # weekday - (optional) a starting day of the week, case insensitive, string. e.g. "tueSday"

    weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    new_weekday = ''

    # start to hours,min and AM/PM
    start_time, start_pm_or_am = start.split()
    start_hrs, start_min = start_time.split(':')

    # duration to hours, min
    duration_hrs, duration_min = duration.split(':')

    # new time calculation
    new_mins = int(start_min) + int(duration_min)
    new_hours = int(start_hrs) + int(duration_hrs) + 12 * (start_pm_or_am == 'PM') + int(new_mins // 60)
    new_mins = new_mins % 60
    new_hours_formatted = '12' if (new_hours % 12 == 0) else str(new_hours % 12)
    # number of "days later"
    if new_hours // 24 == 0:
        days_after = ''
    elif new_hours // 24 == 1:
        days_after = ' (next day)'
    else:
        days_after = ' (' + str(new_hours // 24) + ' days later)'
    day_after_am_or_pm = ' AM' if ((new_hours // 12) % 2 == 0) else ' PM'
    # new weekday, optional
    if len(weekday) > 0:
        new_weekday_index = (weekdays.index(weekday.lower()) + (new_hours // 24)) % 7
        new_weekday = ', ' + weekdays[new_weekday_index].capitalize()

    # final formatted string
    new_time = new_hours_formatted + ':' + str(new_mins).zfill(2) + day_after_am_or_pm + new_weekday + days_after

    return new_time
