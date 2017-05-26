def sum_of_mult(max_index):
    sum_list=[]
    for i in range(max_index):
        if i%3==0 or i%5==0:
            sum_list.append(i)
    return sum(sum_list)
