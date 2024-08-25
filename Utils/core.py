from nbformat.sign import trust_flags
from sympy import false


def area_of_triangle(s11,s22,s33):
    s = (s11 + s22 + s33) / 2
    area = (s * (s - s11) * (s - s22) * (s - s33)) ** 0.5
    return  area

def prime_check(num):
    flag = false
    if( num == 0 or num == 1):
        print(f'Number {num} is not a prime')

    elif num > 1:
        # check for factors
        for x  in range(2,num):
            if(num % x == 0 ):
                flag = True
                break
    #check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num,"is a prime number")



