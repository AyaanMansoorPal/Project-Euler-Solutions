def sum_a(num):
    alist=[]
    for n in range(1,num+1):
        alist.append(n)
    return sum(alist)**2

def sum_b(num):
    olist=[]
    for n in range(1,num+1):
        print(n)
        olist.append(n**2)
    return sum(olist)


def difference(num):
    answer=-sum_b(num)+sum_a(num)
    return answer
        
