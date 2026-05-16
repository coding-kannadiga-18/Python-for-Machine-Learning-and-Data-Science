
# Sum of list elements
nums = [2,6,7,3,45,34]
sum = 0
for num in nums :
    sum += num
print(sum)

# Largest element in list
nums = [2,6,7,3,45,34]
max = 0
for i in range(0,len(nums)-1):
    j = i + 1
    if nums[i] > nums[j]:
        max = nums[i]
    else:
        max = nums[j]
print("The Largest Element in the List is",max) 

# Number of even numbers in a list
nums = [2,6,7,3,45,34]
count = 0
for num in nums:
    if num % 2 == 0:
        count += 1
print(count)

# Reverse a list
nums = [2,6,7,3,45,34]
print(nums[::-1])
size = len(nums)
result = []
for i in range(size):
    ele = nums[size -i -1]  # 6 - 5 -1 = 0 => nums[0] => 2
    result.append(ele)
print(result)

# Check whether element present in list or not
num = int(input("Enter the element : "))
nums = [2,6,7,3,45,34]
if num in nums:
    print("Yes, Number present in List")
else:
    print("Number doesn't exist")