class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        if all(start >= e or end <= s for s, e in self.calendar):
            self.calendar.append((start, end))
            return True
        return False
