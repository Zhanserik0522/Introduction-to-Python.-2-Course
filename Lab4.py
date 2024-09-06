# Laboratory work 4
# 1
sample_tuple = (100, 200, 300)
formatted_string = "This is a tuple {}".format(sample_tuple)
print(formatted_string)
# 2
print("QWERtY")
Sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
for i in Sample_list:
    print(i[:-1] + (new_value,), end="")
# 3
print()
Original_turple = (4, 3, 2, 2, -1, 18)
product = 1
for i in Original_turple:
    product *= i
print(product)
# 4
print()
turple_4 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
for i in turple_4:

    print(sum(i) / len(i), end=" ")
# 5
print()
turle_5 = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('White', 'Yellow', 'Lime'))
word_need_to_check = 'White'
for i in turle_5:
    if word_need_to_check in i:
        print("TRUE")
    else:
        print("FALSE")

# Dictionaries 1
print()
sample_dict = {0: 10, 1: 20}
new_key = 2
new_value = 30

sample_dict[new_key] = new_value

print(sample_dict)
# Dictionaries 2
print()

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result_dict = {}

result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)

print(result_dict)
# Dictionaries 3
print()
sample_dictionary = {1: 1, 2: 4}
n = 5
ans = {}
for i in range(1, n + 1):
    ans[i] = sample_dictionary.get(i, i ** 2)
print(ans)

# Dictionaries 4
print()

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = {}


for key, value in d1.items():
    combined_dict[key] = value

for key, value in d2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print(combined_dict)

# Sets 1
print()
random_set = {10, 20, 30, 40, 50}
largest = max(random_set)
smallest = min(random_set)
print(f"The minimal value of the is - {smallest} ,the maximum value is - {largest}")
# Sets 2
print()
lenth_of_random_set = len(random_set)
print(f"The length of set - is {lenth_of_random_set}")

# Sets 3
print()
value_need_to_check = 10
for i in random_set:
    if value_need_to_check == i:
        print("present")
        break
else:
    print("not present")