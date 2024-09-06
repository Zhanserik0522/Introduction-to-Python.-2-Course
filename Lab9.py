import math


# Ex 1
class MyTime:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def convert_to_second(self):
        total_second = self.hour * 3600 + self.minute * 60 + self.second
        return total_second

    def convert_to_minutes(self):
        total_min = self.hour * 60 + self.minute + self.second / 60
        return total_min


class AnalogTime(MyTime):
    def to_analog_time(self):
        analog_hour = self.hour % 12 if self.hour % 12 != 0 else 12
        return f"{analog_hour:02}:{self.minute:02}:{self.second:02}"

    def to_american_time(self):
        am_pm = 'a.m.' if self.hour < 12 else 'p.m.'
        american_hour = self.hour if self.hour <= 12 else self.hour - 12
        return f"{american_hour:02}:{self.minute:02}:{self.second:02} {am_pm}"


my_time = MyTime(10, 12, 1)
print(my_time.convert_to_second())


# Ex 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

