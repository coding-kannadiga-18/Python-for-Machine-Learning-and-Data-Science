# Creating tuple
nums = (1,2,3,4,5,6)
print(nums)


# Tuple Packing
t = 1,2,3
x = t[0]
y = t[1]
z = t[2]

print(x,y,z)

# Tuple Unpacking
x,y,z = 1,2,3
print(type(x))
print(x,y,z)

# Single element tuple
t = (2,)
print(type(t))

# Using tuple unpacking
pairs = [(1,2),(3,4),(5,6)]
for x,y in pairs:
    print(x,y)

# partial unpacking(* operator)
a,*b = [1,2,3,4]
print(a,b)

# Tuple Operation using List
salary = (10000,15000,20000,25000)
sal = list(salary)

sal[1] = 20000
salary = tuple(sal)

print(salary)
print(sal)
