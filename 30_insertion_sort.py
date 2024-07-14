def insertion_sort(data_list):
    for i in range(1,len(data_list)):
        temp = data_list[i]

        j = i-1
        while j>=0 and temp<data_list[j]:
            data_list[j+1] = data_list[j]
            j-=1
        
        data_list[j+1] = temp
    print(data_list)

insertion_sort([25,37,11,14,60, 82,18,41])