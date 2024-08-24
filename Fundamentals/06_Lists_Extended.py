## source: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Data structure
letters = ['A','B','C','D','E','F','F','G','H']
print('Initial List', letters)

# 1. append(x) -- Adds element at the end of the list
letters.append('I')
print('After Append: ',letters)

# 2. extend() -  extend list by appending all the items from the iterable
letters.extend('J')
print('After  extend: \t',letters)

# 3. insert(i,x) - insert an item at given position
letters.insert(2,'C')
print('After  insert: \t',letters)

#4.  remove(x) - Removes the first item from list whose value is equal to x
letters.remove('C')
print('After remove: \t',letters)

#5.  pop[i] remove the item at the given position in the list and return it. if no index found pop() removes and return last index item
letters.pop(2)
print('After pop: \t',letters)

#6. index(x,[start],[end])  -- return zero based index in the list
print('After index: \t',letters.index('D'))

#7. count(x) : returns number of times x appears in the list
print('Count: \t',letters.count('F'))

#8. sort(*,key=None,reverse=False)
letters.sort()
print('After default sort: \t',letters)
letters.sort(reverse=True)
print('Reverse sort: \t',letters)

#9. copy() - Returns a shallow copy of the list
new_letters = letters.copy()
print('New List: \t',new_letters)




