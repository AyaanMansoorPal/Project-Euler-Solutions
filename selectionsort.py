def selection_sort(L):
    d=[]
    while L !=[]:
        min_val=min(L)
        L.remove(min_val)
        d.append(min_val)
        
    return d
