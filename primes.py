"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    for num in range(1, 500):
        if num>1:
            for i in range(2, num):
                if(num%i)==0:
                    break
            else:
                list.append(num)
    return list[0:number_of_primes]
print(f'first 10 prime numbers are {primes(10)}')