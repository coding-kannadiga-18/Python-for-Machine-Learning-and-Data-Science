"""

# "I love Python" => "Python love I"

a = "I love Python"
b = a.split(" ")
print(b)

result = b[::-1]

rev = " ".join(result)
print(rev)

# vowel => "aeiou"

language = "Python Programming"
result = ""

for vowel in language:
    if vowel not in "aeiou":
        result +=vowel           
print(result)

#Number of words in a sentence 

sentence = "Hi guys, Welcome to my youtube channel"

word = sentence.split(" ")

print(len(word))

# Frequent character in a string

fruit = "Apple"
max_count = 0
max_ch = ""

for i in fruit:
    count = fruit.count(i)          

    if count > max_count:
        max_count = count
        max_ch = i

print(max_ch)

# Remove Frequent character in a string

fruit = "Apple"
max_count = 0
max_ch = ""

for i in fruit:
    count = fruit.count(i)          

    if count > max_count:
        max_count = count
        max_ch = i

result = fruit.replace(max_ch,"")
print(result)

"""


