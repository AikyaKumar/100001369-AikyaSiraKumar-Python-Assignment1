from datetime import datetime, timedelta

YourCalendar = input("Enter your calendar (e.g., [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]): ")
YourWorkingHours = input("Enter your working hours (e.g., ['9:00', '20:00']): ")

YourCoWorkersCalendar = input("Enter your co-worker's calendar (e.g., [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]): ")
YourCoWorkersWorkingHours = input("Enter your co-worker's working hours (e.g., ['10:00', '18:30']): ")

MeetingDuration = int(input("Enter meeting duration in minutes (e.g., 30): "))

ParseYourCalendar = [item.strip(" []").replace("'", "").split(", ") for item in YourCalendar.split("], [")]
ParseYourWorkingHours = YourWorkingHours.strip("[]").replace("'", "").split(", ")

ParseCoWorkersCalendar = [item.strip(" []").replace("'", "").split(", ") for item in YourCoWorkersCalendar.split("], [")]
ParseCoWorkersWorkingHours = YourCoWorkersWorkingHours.strip("[]").replace("'", "").split(", ")

# converting string times to datetime objects
YourCalendar = [(datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M")) for start, end in ParseYourCalendar]
YourCoWorkersCalendar = [(datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M")) for start, end in ParseCoWorkersCalendar]

YourWorkStartTime, YourWorkEndTime = [datetime.strptime(x, "%H:%M") for x in ParseYourWorkingHours]
YourCoWorkersWorkStartTime, YourCoWorkersWorkEndTime = [datetime.strptime(x, "%H:%M") for x in ParseCoWorkersWorkingHours]

# finding the common meeting start and end times possible
CommonStartTime = max(YourWorkStartTime, YourCoWorkersWorkStartTime)
CommonEndTime = min(YourWorkEndTime, YourCoWorkersWorkEndTime)

print(f"The possible meeting start time is: {CommonStartTime.strftime('%H:%M')}")
print(f"The possible meeting end time is: {CommonEndTime.strftime('%H:%M')}")

if CommonStartTime >= CommonEndTime:
    print("No overlapping working hours. No meeting possible.")
else:
    # checking for possible common free slots
    PossibleMeetTime = CommonStartTime
    MeetDuration = timedelta(minutes=MeetingDuration)
    FreeSlots = []

    while PossibleMeetTime + MeetDuration <= CommonEndTime:
        YourFreeTime = True
        for start, end in YourCalendar:
            if not (PossibleMeetTime >= end or PossibleMeetTime + MeetDuration <= start):  
                YourFreeTime = False
                break

        YourCoWorkerFreeTime = True
        for start, end in YourCoWorkersCalendar:
            if not (PossibleMeetTime >= end or PossibleMeetTime + MeetDuration <= start):  
                YourCoWorkerFreeTime = False
                break

        if YourFreeTime and YourCoWorkerFreeTime:
            FreeSlots.append((PossibleMeetTime.strftime('%H:%M'), (PossibleMeetTime + MeetDuration).strftime('%H:%M')))

        PossibleMeetTime += MeetDuration

    if FreeSlots:
        print("Common free slots:", FreeSlots)
    else:
        print("No common free slots found.")

# increment 30 and check

'''
        # Comparing start times
    if YourWorkStartTime < YourCoWorkersWorkStartTime:
        print("# Consider YourCoWorkersStartTime (Your co-worker logged in late, no meeting possible)")

    elif YourWorkStartTime > YourCoWorkersWorkStartTime:
        print("# Consider YourStartTime (You logged in late, no meeting possible)")
    else:
        print("# Both are the same, consider YourStartTime (Meeting can happen)")

    # Comparing end times
    if YourWorkEndTime > YourCoWorkersWorkEndTime:
        print("# Your co-worker left early. No meeting possible.")
    elif YourWorkEndTime < YourCoWorkersWorkEndTime:
        print("# You left early. No meeting possible.")
    else:
        print("# Both are available until the same time. Meeting can happen.")
    return None'''

