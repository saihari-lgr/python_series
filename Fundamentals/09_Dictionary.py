
dict1 = {'1':'one','2':'two','4':'Four'}
print(dict1)
print(dict1.keys())
print(dict1.values())

# Adding new item
dict1['3'] = 'three'
print(dict1)

#looping over dictionaries
#Accessing both key and values using items()
for key,val in dict1.items():
    print(f'key: {key} \t value: {val}')

#looping through a sequence, the position index and corresponding value can be retrieved at the same time
# using the enumerate() function
for ind,val in enumerate(dict1):
    print(f'position: {ind} \t value: {val}')

for ind,val in enumerate(['apple','boy','cat']):
    print(f'position: {ind} \t value: {val}')



