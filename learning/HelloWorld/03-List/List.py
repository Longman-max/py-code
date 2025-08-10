names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names[0:3]) # range
print(names[-1])
print(names)

friends = ["John", "Sam", "Mary"]
for index in range(len(friends)):
    print(friends[index])