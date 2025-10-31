def add(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total

def recursive_factorial(n):
    # temel koşul (base case)
    if n==0 or n==1:
        return 1
    return n * recursive_factorial(n-1)

def recursive_reverse_list(input_list):
    # temel - koşul
    if len(input_list) <= 1:
        return input_list
    return [input_list[-1]] + recursive_reverse_list(input_list[:-1])

def recursive_sum_list(numbers):
    """
    Bir listedeki elemanları toplar. 
    Geriye toplam sonucu döner
    
    Parametre:
    numbers: Numaraları içeren listedir. 
    """
    # temel koşul 
    if len(numbers) == 0:
        return 0
    return numbers[0] + recursive_sum_list(numbers[1:])
