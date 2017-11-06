def problem(n):
    result=n
    while n>1:
        result=(n-1)/result
        n-=1
    print (result)
