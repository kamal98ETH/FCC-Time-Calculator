def add_time(start, duration, dayOpt=None):
    # Capturing intial variabales
    start = start.split()
    bTime = start[0].split(":")
    bH = bTime[0]
    bM = bTime[1]
    bFormat = start[1]

    # Capturing added variables
    duration = duration.split()
    aTime = duration[0].split(":")
    aH = aTime[0]
    aM = aTime[1]

    # Calculating
    if bFormat == "PM":
        bH = int(bH) + 12
    rM = int(bM) + int(aM)
    rH = int(bH) + int(aH) + int(rM / 60)

    # Converting to base 60
    rM = rM % 60
    rD = int(rH / 24)
    rH = rH % 24
    if rH == 0:
        rH = 12
        bFormat = " AM"
    elif rH < 12:
        bFormat = " AM"
    elif rH < 13:
        bFormat = " PM"
    else:
        rH = rH - 12
        bFormat = " PM"

    # Calculating the day
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    if dayOpt != None:
        dayOpt = dayOpt.capitalize()
        for i in range(7):
            if dayOpt == days[i]:
                j = (i + rD) % 7
                day = ", " + days[j]
    else:
        day = ""

    # Remaining day(s)
    if rD > 1:
        raimaining = " (" + str(rD) + " days later)"
    elif rD == 1:
        raimaining = " (next day)"
    else:
        raimaining = ""

    # Displaying
    rM = str(rM)
    rH = str(rH)
    if len(rM) < 2:
        rM = "0" + rM
    new_time = rH + ":" + rM + bFormat + day + raimaining

    return new_time
