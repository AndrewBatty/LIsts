# Andrew Batty
# Lists starter 1
# 10/12/14

result = 0
index = 0

for count in range(0,4):
    values = int(input("Please enter a value: "))
    index = index + 1
    if result < values[index]:
        result = values[index]
        print(result)

