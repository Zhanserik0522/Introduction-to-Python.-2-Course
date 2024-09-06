# Ex 1
def positive_odd_numbers(number_list):
    return [num for num in number_list if num > 0 and num % 2 != 0]


def convert_to_positive(number_list):
    return [abs(num) for num in number_list]


def count_positive_odd_numbers(number_list):
    return len([num for num in number_list if num > 0 and num % 2 != 0])


def average_number(number_list):
    return int(sum(number_list) / len(number_list))


def average_positive_negative_numbers(number_list):
    positive_numbers = [num for num in number_list if num > 0]
    negative_numbers = [num for num in number_list if num < 0]

    avg_positive = 0 if len(positive_numbers) == 0 else int(sum(positive_numbers) / len(positive_numbers))
    avg_negative = 0 if len(negative_numbers) == 0 else int(sum(negative_numbers) / len(negative_numbers))

    return avg_positive, avg_negative


def replace_negative_with_zero(number_list):
    return [num if num >= 0 else 0 for num in number_list]


# Ex 2
def sum_of_n_integers(n):
    return sum(range(1, n+1))


# Ex 3
def generate_short_fibonacci():
    fib_sequence = [1, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > 32767:
            break
        fib_sequence.append(next_fib)
    return fib_sequence




