i = 0
with open('user.txt', 'r') as f:
    for line in f:
        i += 1
print(i)