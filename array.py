# setup the data structure
f = open('in.txt')
nums=[]
for line in f:
    nums.append(int(line.strip()))
# insertion --> insert at random place
nums.insert(3,1000)
print(nums)
# deletion --> remove
nums.remove(1996)
print(nums)
# appending --> insert at the end
nums.append(2000)
print(nums)
# retrival --> search
t=int(input())
if t in nums:
    print("Found")
# update --> update at a given index
nums[1990]="Defence Institute"
print(nums)