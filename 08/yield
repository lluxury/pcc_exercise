import math

def get_primes3(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append()

    return result_list

def get_primes2(input_list):
    return (element for element in input_list if is_prime(element))

def get_primes4(number):
    while True:
        if is_prime(number):
            yield number
        number +=1


def is_prime(number):
    if number >1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number)+1),2):
            '''#开方取整,math没定义'''
            if number % current == 0:
                return False
            return True
    return False
    '''#感觉最后一个return是保险,避免内部出错误导结果'''

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return


def print_successsive_primes(iterations, base=10):
    #参数
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

def get_primes(number):
    while  True:
        if is_prime(number):
            number = yield number
        number += 1
        
#solve_number_10()
#新特性 看不懂