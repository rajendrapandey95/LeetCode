class MyCalendarTwo:
    def __init__(self):
        self.bookings, self.overlap_bookings = [], []

    def book(self, start: int, end: int) -> bool:
        if any(max(s1, start) < min(e1, end) for s1, e1 in self.overlap_bookings):
            return False
        self.overlap_bookings += [(max(s1, start), min(e1, end)) for s1, e1 in self.bookings if max(s1, start) < min(e1, end)]
        self.bookings.append((start, end))
        return True
