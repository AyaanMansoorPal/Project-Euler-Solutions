def merge(A,B):
    d=[]
    
    while A!=[] and B!=[]:
        max_val=max(A[len(A)-1],B[len(B)-1])
        if max_val in A:
            A.remove(max_val)
            d.append(max_val)
        elif max_val in B:
            B.remove(max_val)
            d.append(max_val)

    if A==[]:
        B.reverse()
        d=d+B
    else:
        A.reverse()
        d=d+A
    d.reverse()
    return d
    
    
        
        
        
        
