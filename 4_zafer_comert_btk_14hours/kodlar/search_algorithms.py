def linear_search(input_list, target):
    """Doğrusal arama

    Args:
        input_list (list): Arama yapılacak liste
        target (item): Hedef değer

    Returns:
        int: Aranan elemanın liste içerisindeki indis değeri 
    """
    for i in range(len(input_list)):
        if input_list[i]==target:
           return i 
    return -1

def binary_search(arr, target,left,right):
    # temel koşul
    if left > right:
        return -1
    
    # ortanca
    mid = (left+right)//2
    
    # hedef değer
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr, target, left, mid-1)
    else:
        return binary_search(arr, target, mid+1, right)