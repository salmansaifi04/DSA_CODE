def selection_sort(data_list):
    n = len(data_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if data_list[j]<data_list[min_index]:
                min_index = j
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    print(data_list)

selection_sort([34,67,12,89,25,50])