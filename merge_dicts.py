def merge_dicts(dict1, dict2):# Python code to merge dict using update() method
    return(dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(merge_dicts(dict1, dict2))#returns none
print(dict2)#prints the merged dicts