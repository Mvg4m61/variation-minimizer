def minimize():
    
    l1 = []
    n = int(input("\nEnter number of packets: "))
    for i in range(n):
        num = int(input("Enter number of sweets respectively (Must be a positive integer): "))
        l1.append(num)
    m = int(input("\nEnter number of children: "))
    l1.sort(reverse=True)
    print(l1)
    diff = l1[0]-l1[m-1]
    for i in range(1,n-m+1):
        d = l1[i]-l1[i+(m-1)]
        if d<diff:
            diff=d       
 
    print("\nMinimum difference: ",diff)
minimize()