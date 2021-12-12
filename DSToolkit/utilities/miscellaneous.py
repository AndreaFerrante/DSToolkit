import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random
import math
import tqdm


arr = [9,3,5,6,2,1,4,7,8,11,12,23,21,45,30]


def get_median(arr):

	arr = sorted(arr)
	n   = len(arr) - 1

	if n % 2 == 1:
		return (arr[ n // 2 ] + arr[ (n // 2) + 1 ]) / 2
	else:
		return arr[ n // 2 ]


def get_most_frequent(arr:list):

    # from collections import Counter
    # most_frequent = Counter(arr).most_common()[0][0]

    common = {}

    for el in arr:
        if el in common.keys():
            common[el] += 1
        else:
            common[el] = 1

    max, max_el = 0, 0

    for key, value in common.items():
        if value > max_el:
            max_el = value
            max    = key

    return max


def gcd_(a, b):

    '''
    GREATEST COMMON DIVISOR
    '''

    max_value  = max(a, b)
    common_div = 0

    for i in range(1, max_value):
        if a % i == 0 and b % i == 0:
            common_div = i

    return common_div


def pow_1(n, power):

    n_power = 0

    for i in range(1, power + 1):
        if i != 1:
            n_power = n_power * n
        else:
            n_power = n

    return n_power


def pow_2(base, exp):

	res = 1

	for i in range(exp):
		res = res * base

	return res


def str_reverser_1(str_to_reverse:str=''):

	if str_to_reverse != '':
		return str_to_reverse[::-1]
	else:
		return None


def str_reverser_2(str_reverse:str) -> str:

    len_str = len(str_reverse)
    len_fin = ''

    for i in range( len_str ):
        len_fin += str_reverse[(len_str-i-1):len_str-i]

    return len_fin


def get_rolling_mean(period:int, array:list):

    # array  = np.cumsum( [np.random.normal() for x in range(100)] )
    # period = 5

    rolling_mean = []
    for i in range( 1, len(array)-period ):
        rolling_mean.append( np.sum(array[ i :( i+period )]) / period )

    pd.Series(array[period:]).plot()
    pd.Series(rolling_mean).plot()


def get_prime_number_0(n:int)->tuple:

    primes   = []
    for i in range(2, n + 1):
        pcounter = 0
        for j in range(2, i + 1):
            if i % j != 0:
                pcounter += 1
            elif pcounter + 2 == i:
                primes.append(i)

    return (len(primes), primes)


def get_prime_number_1(start, stop):

    if start <= 0:
        start = 1

    primes = []
    for i in range(start, stop):
        prime = 1
        for j in range(2, i):
            if i % j == 0:
                prime = 0
                break
        if prime:
            primes.append(i)

    return primes


def get_prime_number_2(start, stop):

    primes = []

    for i in range(start, stop):
        if all(i % j != 0 for j in range(2, i)):
            primes.append(i)

    return primes


def get_fibonacci_series(end):

    if end < 3:
        print('Gimme at least 3 values !')

    fibo = [0, 1]

    for i in range(1, end):
        fibo.append( fibo[i-1] + fibo[i] )

    return fibo


def rec_fibo(n):

    if n <= 1:
        return n
    else:
        return rec_fibo(n-1) + rec_fibo(n-2)


def get_montecarlo(reps:int=75, lengths:int=1000):

    paths = []
    norms = []
    cums  = 0

    for rep in range(reps):

        paths.append(cums)

        for length in range(lengths):
            cums += random.gauss(0, 1)
            paths.append(cums)

        plt.plot(paths, linewidth=0.75)
        norms.append(cums)
        paths = []
        cums  = 0

    return norms


def get_binomial(n:int=5, event:int=2, p:float=0.25):

    def get_combination(n_:int, event_:int):

        num = math.factorial(n_)
        den = math.factorial(event_) * math.factorial(n_ - event_)
        return num / den

    binomial = (get_combination(n, event)) * (p ** event) * ((1 - p) ** (n - event))

    return binomial


def generator(max):
    number = 1
    while number < max:
        number += 1
        yield number


def get_reservoir_sampling(k):

    stream = generator(10000)

    reservoir = []
    for i, el in enumerate(stream):
        if i + 1 <= k:
            reservoir.append(el)
        else:
            proba = k / (i + 1)
            if random.random() < proba:
                reservoir[ random.choice( [range(k)] ) ] = el

    return reservoir


def get_longest_consec(input_str:str='') -> dict:

    ret_dict  = {}
    max_count = 1

    for idx, el in enumerate(input_str[1:], start=1):
        if el == input_str[idx-1]:
            max_count += 1
            if el in ret_dict.keys():
                if max_count > ret_dict[el]:
                    ret_dict[el] = max_count
            else:
                ret_dict[el] = max_count
        else:
            max_count = 1

    max_key = max(ret_dict, key=ret_dict.get)

    return max_key, ret_dict[max_key]


def get_unique_values_in_list(arr):

    tmp_lst = []
    tmp_lst.append(arr[0])

    for i in arr:
        if i not in tmp_lst:
            tmp_lst.append(i)

    return tmp_lst


def dec_example(function):

    def inner(*args, **kwargs):

        print('Decorator args -->', *args)
        temp = function(*args, **kwargs)
        print('Decorator return -->', temp + 1)

    return inner


@dec_example
def decorator_printer(str_input):
    print('Print inside main function is', str_input)
    return 1
decorator_printer('My first decorator...')


class A:
    def rk(self):
        print(" In class A")

class B(A):
    def rk(self):
        print(" In class B")

class C(B, A):
    def rk(self):
        print(" In class C")

class D(C, A, B):
    def rk(self):
        print(" In class D")

r = D()
r.rk()


