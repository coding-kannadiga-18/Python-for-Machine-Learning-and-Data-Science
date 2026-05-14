"""

data = ["Rahul", 21, "6th std", 90]
print(type(data))
print(data)

print(data)
data.append(12)
data.remove(21)
print(data)


for i in range(len(data)):
    print(i, data[i])

print()
print(len(data))

"""

df = []
print(df)
for i in range(3):
    ele = input("Enter Fruits name : ")
    df.append(ele)

print(df)