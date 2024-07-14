def bubble_sort(data_list):
    count_var = 0
    for r in range(1, len(data_list)):
        count_var += 1
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
    print(data_list, count_var)

bubble_sort([34,67,12,89,25,50])

def modified_bubble_sort(data_list):
    count_var = 0
    for r in range(1, len(data_list)):
        count_var += 1
        swapping_flag = False
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
                swapping_flag = True
        if swapping_flag == False:
            break
    print(data_list, count_var)
modified_bubble_sort([34,67,12,89,25,50])