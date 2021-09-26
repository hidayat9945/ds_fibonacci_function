def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here

import math
def matematika(x):
 n = int(math.sqrt(x))
 return n*n == x
def find_fibonacci(n):
 
 return matematika(5*n*n + 4) or matematika(5*n*n - 4)
 
for i in range(1,20):
 if (find_fibonacci(i) == True):
  print(i,"adalah sebuah angka fibonacci")
 else:
  print(i,"BUKAN sebuah angka fibonacci ")



if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))
