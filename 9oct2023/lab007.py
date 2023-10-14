# string its a bunch of char
#string cant be changed

name = "fadhel"
# capitalize return a copy of string with 1sh char capital
result = name.capitalize()
print(result)
print(name)

print(id(name))
print(id(result))
#upper case

result2 = name.upper()
print(result2)

#lower case

result3 = name.lower()
print(result3)

#swap case change small to capital and viseversa
name = "FadHeL"
print(name.swapcase())


#title makes the first letter from the word capital

name2 = "hello world"
print(name2.title())

#replace
text = "hello world"
result2 = text.replace("world","python")
print(result2)

#find return the lowest index of substring in the string
#return -1 if the substring not found

text = "hello world"
index = text.find("world")
print(index)

#count(count the char)
count = text.count("l")
print(count)




