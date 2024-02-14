def genHours():
    hours = []
    for hour in range(24):
        hours.append(hour)
        if hour > 12:
            hour - 12
            hours.append(hour)
    return hours
