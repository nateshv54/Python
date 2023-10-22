'''Python Program for Permutations 
In Which N People Can Occupy R Seats In A Classroom'''
'''In a classroom some of the seats are already occupied by students
 and only a few seats are available in the classroom. 
 The available seats are assumed as r and n number of students are
   looking for the seat. We need to find in how many different 
   permutations n number of students can sit on r number of chairs'''
#Algorithm
'''Input number of students in n
Input number of seats in r
Use permutation formula { factorial(n) / factorial(n-r) }
Print Output'''

n=int(input())
r=int(input())
def fact(f):
    if(f<=1):
        return 1
    return f*fact(f-1)

permutation=fact(n)//fact(n-r)
print("Permutations are",permutation)

#Number of Handshakes for n no.of students
handshakes=(n*(n-1))//2
print("The No.of handshakes will be",handshakes)