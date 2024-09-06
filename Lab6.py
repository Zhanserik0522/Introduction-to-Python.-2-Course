# Exercise 1
x_1 = 7 + 3 * 6 / 2 - 1
x_2 = (3 * 9 * (3 + (4 * 5/3)))
x_3 = 12.0 + 2 / 5 * 10.0
x_4 = 2/5 + 10.0 * 3 - 2.5

print(x_1, x_2, x_3, x_4,sep="\t")

# Exercise 2


def convert_into_celsius(temp_in_fr):
    celsius = (5 / 9) * (temp_in_fr - 32)
    return celsius

temp = 212
print(convert_into_celsius(temp))

# Exercise 3
p = 3.14159


def circle_parameters(radius):
    diameter = 2 * radius
    circumference = 2 * p * radius
    area = p * radius ** 2
    print(f"The diameter,circumference,area has the value - '{diameter}','{circumference}','{area}'")


circle_parameters(10)
# Exercise 4


def distance_between_2point(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d


print(distance_between_2point(5, 6, 7, 8))
# Exercise 5


def watch(seconds):
    hours = int(seconds / 3600)
    minutes = int(seconds /60 % 60)
    seconds = seconds - minutes * 60 - hours * 3600
    print(f"hh.mm.ss - {hours, minutes, seconds}")


watch(100000)
# Exercise 6


def calculate_change(amount_inserted, item_cost):
    change = amount_inserted - item_cost
    coins = [50, 20, 10, 5, 2, 1]
    change_count = {}

    for coin in coins:
        num_coins = change // coin
        if num_coins > 0:
            change_count[coin] = num_coins
            change -= num_coins * coin

    return change_count2


print(calculate_change(100, 45))