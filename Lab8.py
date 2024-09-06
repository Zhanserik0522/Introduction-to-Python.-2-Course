# Ex 1
class MyTime:
    def __init__(self, total_seconds=0):
        self.hour = total_seconds // 3600
        self.minute = (total_seconds % 3600) // 60
        self.second = total_seconds % 60

    def set_time_by_seconds(self, total_seconds):
        self.hour = total_seconds // 3600
        self.minute = (total_seconds % 3600) // 60
        self.second = total_seconds % 60

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


seconds_input = 3661
my_time = MyTime(seconds_input)
print(my_time)

# Ex 2


class MyListClass:
    def __init__(self, input_list=None):
        if input_list is None:
            self.my_list = []
        else:
            self.my_list = [int(i) for i in input_list]  # Ensuring all elements are integers

    def get_max(self):
        return max(self.my_list)

    def get_min(self):
        return min(self.my_list)

    def get_same_numbers(self):
        return list(set(self.my_list))

    def get_same_numbers_count(self):
        return {number: self.my_list.count(number) for number in set(self.my_list)}

    def get_sum(self):
        return sum(self.my_list)


# Example usage:
my_list = MyListClass([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print("Max value:", my_list.get_max())
print("Min value:", my_list.get_min())
print("Same numbers:", my_list.get_same_numbers())
print("Same numbers count:", my_list.get_same_numbers_count())
print("Sum of list:", my_list.get_sum())
