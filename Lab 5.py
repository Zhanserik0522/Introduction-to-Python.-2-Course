# Step 1. Reading data from text files
print("Step 1")

with open('user_ids.txt', 'r') as f:
    for line in f:
        print(line)
print()

# Step 2. Reading file content into list
print("Step 2")
with open('user_ids.txt', 'r') as f:
    for line in f:
        print(line.strip())

user_ids = []
with open('user_ids.txt', 'r') as f:
    for line in f:
        user_id = line.strip()
        user_ids.append(user_id)
print(user_ids)
print()

# Step 3. Count the unique numbers of elements
print("Step 3")
print(f"The number of items in list is equal to {len(user_ids)}")
unique_ids = set(user_ids)
print( 'Unique IDs in the file  {}'.format(len(unique_ids)))
print(print(f"The number of unique items in list is equal to {len(unique_ids)}"))

# Files with headers and multiple columns
# Step 1. Reading header files
print("Step 1")
with open('user_ids_header.txt', 'r') as f:
    for line in f:
        print(line.strip())
print()

# Step 2. How avoid the first line
print("Step 2")
Started = True
with open('user_ids_header.txt', 'r') as f:
    for line in f:
        # "if Started"  is equivalent to "if Started == True"
        if Started == True:
            # this line is executed once only on the first step of the loop
            Started = False
        else:
            # this line is executed from the second and in all the next steps of the loop
            print(line.strip())

print()

print("Step 3")
with open('data_3_columns.txt', 'r') as f:
    for line in f:
        line_1 = line.strip().split(" ")
        print(line_1)

print()

# Step 4. Splitting columns

print("Step 4")
with open('data_3_columns.txt', 'r') as f:
    for line in f:
        line = line.strip().split(' ')
        medium = line[0]
        source = line[1]
        amount_paid = line[2].replace(',', '.')
        print(line)
        print(source, medium, amount_paid)


print()

# Step 5. Get a number from the string line
print("Step 5")
with open('data_3_columns.txt', 'r') as f:
    for line in f:
        line = line.strip().split(' ')
        medium = line[0]
        source = line[1]
        amount_paid = float(line[2].replace(',', '.'))
        print(source, medium, amount_paid)

print()

# Step 6. Counting the amount in files
print("Step 6")
sum = 0
with open('data_3_columns.txt','r') as f:
    for line in f:
        line = line.strip().split(" ")
        medium = line[0]
        source = line[1]
        amount_paid = float(line[ 2 ].replace(',', '.'))
        sum += amount_paid
        print(source, medium, amount_paid)
print(sum)
print()


# Step 7. Counting amount with filter
print("Step 7")
total_sum_of_google = 0
total_sum_of_yandex = 0

with open('data_3_columns.txt', 'r') as f:
    for line in f:
        line = line.strip().split(' ')
        medium = line[0]
        source = line[1]
        amount_paid = float(line[2].replace(',', '.'))
        if source == 'yandex':
            total_sum_of_google += amount_paid
            print('Current expenses google: {:.2f}'.format(total_sum_of_google))
        if source == 'google':
            total_sum_of_yandex += amount_paid
            print('Current expenses yandex: {:.2f}'.format(total_sum_of_yandex))

print()
