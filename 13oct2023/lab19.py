#Identity Operators:
# is Returns True if both variables are the same object
# is not Returns True if both variables are not the same object

# x = #Identity Operators:
# is Returns True if both variables are the same object
# is not Returns True if both variables are not the same object

x = [1,2,3]
y = [1,2,3]


print(x is y) #False because its stored diffrently in memory ,diffrent id also

print(id(x))
print(id(y))

print(x is not y) #True
# is used with set,list,dict
