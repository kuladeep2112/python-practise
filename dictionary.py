# setup the data structure
f = open('in.txt')
numbers  = {}
for line in f:
    value = int(line.strip())
    numbers[value] = True

# deletion --> remove
del numbers[1996]

# appending --> insert at the end
numbers[2999]=numbers.pop(1990)
numbers[3000]=numbers[1991]
del numbers[1991]

# retrival --> search
t=int(input())
if t in numbers:
    print("Found")

# update --> update at a given index
nums={1991:False}
numbers.update(nums)

print(numbers)

