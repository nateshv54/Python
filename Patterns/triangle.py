#traingle pattern in python
def triangle(n):
    c=n-1
    for i in range(1,n+1):
        for j in range(1,c+1):
            print(end=' ')
        c=c-1
        for k in range(1,i+1):
            print("*",end=' ')
        print('\r')
triangle(5)

'''
Output:
    * 
   * *
  * * *
 * * * *
* * * * *
'''