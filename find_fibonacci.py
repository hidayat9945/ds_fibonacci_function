def find_fibonacci(num: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    n1, n2 = 0, 1
    count = 0
    res = []
    if (num < 0):
        print("Your number is negative")
    else:
      while (count < num+3):
        res.append(n1)
        # print(n1)
        nth = n1 + n2
        #update
        n1 = n2
        n2 = nth
        count += 1
    # print(res)

    print(num)
    if (num in res):
        return True
    else:
        return False