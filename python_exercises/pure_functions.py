# map, filter, zip, and reduce
from functools import reduce
my_list=[1,2,3]
your_list=[10,20,30]
their_list=(3,4,6)

def mutiply_by2(item):
    return item*2
def only_odd(item):
    return item % 2 != 0
def accumulator(acc,item):
    print(acc,item)
    return acc + item

print(list(map(mutiply_by2, my_list)))
print(list(filter(only_odd, my_list)))
print(list(zip(my_list,your_list,their_list)))
print(reduce(accumulator,my_list))
print(my_list)  