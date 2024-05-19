def highest_even(list):
    even_numbers=[]
    for num in list:
        if num %2 ==0 :  
            even_numbers.append(num)
    return max(even_numbers)
print(highest_even([1,3,4,6,8]))