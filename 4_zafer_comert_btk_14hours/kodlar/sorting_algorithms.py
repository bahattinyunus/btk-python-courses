def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list

def selection_sort(numbers):
    """Seçmeli sıralama algoritmasıdır.

    Args:
        numbers (list): Sıralanacak listedir.

    Returns:
        list: Sıralanmış dizi
    """
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if numbers[j]<numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

def insertion_sort(numbers):
    """Eklemeli (insertion sort) sıralama algoritmasıdır.

    Args:
        numbers (list): Sıralanacak liste

    Returns:
        list: Sıralı liste
    """
    for i in range(1,len(numbers)):
        key = numbers[i]
        j = i-1
        
        while j>=0 and numbers[j]>key:
            numbers[j+1] = numbers[j]
            j-=1
        numbers[j+1] = key
    return numbers

def merge_sort(arr):
    # temel koşul
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)
    
def merge(left, right):
    result = []
    i = j = 0
    
    # sıralı bir şekilde birleştirme işlemi
    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    # Geriye kalan elemanları ekle
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result