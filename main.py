'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def isEven(num):
    return num % 2 == 0

def partition(col, callback):
    truthy_list = []
    falsy_list = []
    for num in col:
        result = callback(num)
        if result:
            truthy_list.append(num)
        else:
            falsy_list.append(num)

    return [truthy_list, falsy_list]


print(partition([1, 2, 3, 4], isEven))


# List comprehension version
# def partition(lst, fn):
#     return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
