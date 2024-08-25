#source: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

fruits = {'apple','mango','banana','apple','mango'}
print(fruits)   #Note: values printed removing duplicates

#membership check
print('apple' in fruits)
print('orange' in fruits)

#empty set
s1 = ()
print(type(s1))  # Note: empty () is treated as tuple

s2 = set()
print(type(s2))  #Note: need to use method set()

#Demonstrating set operations
f1 = set('banana')
print('f1',f1) # <-- unique letters {'a', 'n', 'b'}
f2 = set('apple') # <-- unique letters {'p', 'e', 'a', 'l'}
print('f2',f2)

print('f1 - f2',f1 - f2) # letters in a not in b            {'b', 'n'}
print('f1 | f2',f1 | f2) # letters in a but not in b        {'p', 'b', 'a', 'l', 'e', 'n'}
print('f1 & f2',f1 & f2) # letters in both a and b          {'a'}
print('f1 ^ f2',f1 ^ f2) # letters in a or b but not in both {'p', 'b', 'e', 'l', 'n'}









