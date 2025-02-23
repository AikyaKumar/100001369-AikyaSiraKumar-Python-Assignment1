from datetime import datetime, timedelta

class MeetingScheduler:
    def __init__(self):
        self.YourCalendar = input("Enter your calendar (e.g., [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]): ")
        self.YourWorkingHours = input("Enter your working hours (e.g., ['9:00', '20:00']): ")

        self.YourCoWorkersCalendar = input("Enter your co-worker's calendar (e.g., [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]): ")
        self.YourCoWorkersWorkingHours = input("Enter your co-worker's working hours (e.g., ['10:00', '18:30']): ")

        self.MeetingDuration = int(input("Enter meeting duration in minutes (e.g., 30): "))

        self.parse_inputs()

    def parse_inputs(self):
        self.YourCalendar = [item.strip(" []").replace("'", "").split(", ") for item in self.YourCalendar.split("], [")]
        self.YourWorkingHours = self.YourWorkingHours.strip("[]").replace("'", "").split(", ")

        self.YourCoWorkersCalendar = [item.strip(" []").replace("'", "").split(", ") for item in self.YourCoWorkersCalendar.split("], [")]
        self.YourCoWorkersWorkingHours = self.YourCoWorkersWorkingHours.strip("[]").replace("'", "").split(", ")

        self.YourCalendar = [(datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M")) for start, end in self.YourCalendar]
        self.YourCoWorkersCalendar = [(datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M")) for start, end in self.YourCoWorkersCalendar]

        self.YourWorkStartTime, self.YourWorkEndTime = [datetime.strptime(x, "%H:%M") for x in self.YourWorkingHours]
        self.YourCoWorkersWorkStartTime, self.YourCoWorkersWorkEndTime = [datetime.strptime(x, "%H:%M") for x in self.YourCoWorkersWorkingHours]

    def OurCommonFreeSlots(self):
        CommonStartTime = max(self.YourWorkStartTime, self.YourCoWorkersWorkStartTime)
        CommonEndTime = min(self.YourWorkEndTime, self.YourCoWorkersWorkEndTime)

        if CommonStartTime >= CommonEndTime:
            print("No overlapping working hours. No meeting possible.")
            return

        PossibleMeetTime = CommonStartTime
        MeetDuration = timedelta(minutes=self.MeetingDuration)
        FreeSlots = []

        while PossibleMeetTime + MeetDuration <= CommonEndTime:
            YourFreeTime = all(
                PossibleMeetTime >= end or PossibleMeetTime + MeetDuration <= start
                for start, end in self.YourCalendar
            )

            YourCoWorkerFreeTime = all(
                PossibleMeetTime >= end or PossibleMeetTime + MeetDuration <= start
                for start, end in self.YourCoWorkersCalendar
            )

            if YourFreeTime and YourCoWorkerFreeTime:
                FreeSlots.append((PossibleMeetTime.strftime('%H:%M'), (PossibleMeetTime + MeetDuration).strftime('%H:%M')))

            PossibleMeetTime += MeetDuration

        if FreeSlots:
            print("Common free slots:", FreeSlots)
        else:
            print("No common free slots found.")

scheduler = MeetingScheduler()
scheduler.OurCommonFreeSlots()



