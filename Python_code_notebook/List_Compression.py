"""
nums = [1,2,3,4,5,6]
=> Create list of cubes
=> Create list of numbers divisible by 3

nums = [10,15,20,25,30]
=> Create list "even" if number is even,  "odd" if number is odd

words = ["hi", "hello", "world", "a"]
=> Create list of words with length > 2

"""
nums1 = [1,2,3,4,5,6]
# List of Cubes
cubes = [i ** 3 for i in nums]
print(cubes)

# Divisible by 3
div_by_3 = [i for i in nums if i%3 == 0]
print(div_by_3 )

nums2 = [10,15,20,25,30]
# Even or Odd
even_or_odd = ["Even" if num % 2 == 0 else "Odd" for num in nums]
print(even_or_odd)

words = ["hi", "hello", "world", "a"]
#Length of strings greater than 2
result = [word for word in words if len(word) > 2]
print(result)