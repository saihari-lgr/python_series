print('Demonstrating variable assignments')

a = 10
print('Initial Value a= ',a)

#Assigning 'a' to some other value
a = 20
print('Value of a= ',a)

#Re Assigning variable 'a'

a = a + 1
print('Value of a= ',a)

print('Demonstrating Dynamic typing')
# Pros: very easy to work and faster development time
# Cons: may result in un expected error and we need to aware of type()
my_val = 2

print(f'type of my_val {type(my_val)}  and value {1}',my_val)

my_val = ['Apple', 'Mango']
print(f'type of my_val {type(my_val)}  and value {1}',my_val)

income = 100
tax_slab = 0.1
tax_payable = income * tax_slab
print(f'Tax payable:  \t',tax_payable)




