def find_fibonaci(num):
    list_fibo=[]
    n=0
    b=1
    for a in range(1,num+2) :
        if len(list_fibo) >= 2:
            list_fibo.append(list_fibo[n-1]+list_fibo[n-2])
        else:
            list_fibo.append(b)
        n += 1
        if num in list_fibo:
            return True
        else:
            return False

data1=fin_fibonaci(40)
print(data1)

