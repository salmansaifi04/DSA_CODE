def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot=data_list[0]
        lesser = [x for x in data_list[1:] if x <=pivot]
        greater = [x for x in data_list[1:] if x>=pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
print(quick_sort([25,37,11,14,60, 82,18,41]))



# it is a divide and conquer technique