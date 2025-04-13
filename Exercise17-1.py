class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds_since_midnight = hour * 3600 + minute * 60 + second

    def time_to_int(self):
        return self.seconds_since_midnight
    
    def int_to_time(self, seconds):
        return Time(0, 0, seconds)
    
    def __str__(self):
        hours, remainder = divmod(self.seconds_since_midnight, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.int_to_time(self.time_to_int() + other.time_to_int())
        else:
            return self.int_to_time(self.time_to_int() + other)
    
    def __sub__(self, other):
        return self.int_to_time(self.time_to_int() - other.time_to_int())
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

# Example test code (should remain unchanged)
t1 = Time(9, 45, 0)
t2 = Time(1, 35, 0)
print(t1)  # Expected: 09:45:00
print(t2)  # Expected: 01:35:00
t3 = t1 + t2
print(t3)  # Expected: 11:20:00
t4 = t1 - t2
print(t4)  # Expected: 08:10:00
print(t1.is_after(t2))  # Expected: True
