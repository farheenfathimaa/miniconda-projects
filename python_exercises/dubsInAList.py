# Exercise: Check for dublicates in list:
some_list=['a','b','c','d','b','i','n','n']
dubs_list=[]
for object in some_list:
    if  some_list.count(object) > 1:
        if object not in dubs_list:
            dubs_list.append(object)
print(dubs_list)