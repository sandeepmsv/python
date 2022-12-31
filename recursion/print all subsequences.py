def printF(ind,ds,arr,n):
    if(ind==n):
        for i in ds:
            print(i,end = " ")
        if(not len(ds)):
            print("{}")
        print()
        return 
    # take or pick the particular index into the subsequence
    ds.append(arr[ind])
    printF(ind+1,ds,arr,n)
    ds.pop()
    # not pick, or not take condition, this element is not added to your subsequence
    printF(ind+1,ds,arr,n)
  
    
    
    
    



arr = [3,1,2]
ds = []
printF(0,ds,arr,len(arr))