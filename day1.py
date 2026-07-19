#13-07-2026

""" 1.
for i in range(1,11):
    print(f"{i}x 9 = {i*9}")

"""

"""2.#Sum on n natural numbers

n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
"""

"""
3. #Factorial

n=int(input())
r=1; 
for i in range(1,n+1):      #alternate math.factorial(n)
    r*=i
print(r)

"""

"""
#LCM of 2 numbers        math.lcm(n,m)

a,b = map(int,input().split())
m=max(a,b)
for i in range(m,a*b,m):    #max---product---with an interval of max among 2
    if i%a==0 and i%b==0:
        LCM= i
        print(LCM)
        break
        
"""

"""
#HCF or GCD of 2 numbers
    # HCF ranges between 1 to min value among 2

a,b = map(int,input().split())
m=min(a,b)
for i in range(m,1,-1):
    if a%i==0 and b%i==0:
        HCF=i
        print(HCF)
        break

"""

"""
# GCD logic

a,b = map(int,input().split())
m=max(a,b)
n=min(a,b)

while m%n!=0:
    r=m%n
    m=n
    n=r
print(r)

"""

"""
#Fibonacci  nth fib no

a=int(input())
m=0
n=1
for i in range(a):
    p=m+n
    m=n
    n=p
print(m)

"""

"""
#pattern printing

n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

"""
"""
#pattern printing 2

n=int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""

#pattern printing 3
"""
r,c=map(int,input().split())

for i in range(1,r+1):
    for j in range(1,c+1):
        print(f"({i},{j})",end=" ")
    print()

"""

"""
#Pattern FRAME

f=int(input())

for i in range(1,f+1):
    for j in range(1,f+1):
        if i==1 or j==f or i==f or j==1:
            print("*",end=" ")
        else:
            print("-",end=" ")
    print()

"""

"""
#Pattern FRAME 2

f=int(input())

for i in range(1,f+1):
    for j in range(1,f+1):
        if i==j or i+j==f+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""

#  14-07-2026
"""  
  n=5

for i in range(1,n+1):
    print(i*"*",end=" ")

#Output :  * ** *** **** *****
 
"""

"""
n=int(input())

    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

#Output: 

* 
* * 
* * * 
* * * * 

"""

"""
n=int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#Output
1
2 2
3 3 3
4 4 4 4
"""

"""
N=int(input())
n=2*N-1

for r in range(1,n+1):
    for j in range(1,n+1):
        if r==j or r+j==n+1:
            print(" ",end='')
        else:
            print("*",end='')
    print()
#Output:

 ******* 
* ***** *
** *** **
*** * ***
**** ****
*** * ***
** *** **
* ***** *
 ******* 
 
 """

"""Diamond pattern

n=int(input())


for i in range(1,n+1):
    #spaces
    for j in range(1,n-i+1):
        print(" ",end='')
        
    for k in range(1,2*i):
        print("*",end='')
    print()
    
for i in range(n,0,-1):
    #spaces
    for j in range(1,n-i+1):
        print(" ",end='')
        
    for k in range(1,2*i):
        print("*",end='')
    print()

#Output:
   *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

"""
"""number pyramid
n=int(input())

for i in range(1,n+1):
    #spaces
    for j in range(1, n-i+1):
        print(' ',end='')
    #numbers 
    temp=i
    for k in range(1,2*i):
        print(temp,end='')
        if k<i:
            temp+=1
        else:
            temp-=1
    print()
#Output:
        1
       232
      34543
     4567654
    567898765

"""

""" Albhabet Pyramid
n=int(input())
ch = 65
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for k in range(1,i+1):
        print(chr(ch),end='')
        ch+=1
        if ch>90:
            ch=65
    print()

#Output:
   A 
  BC
 DEF
GHIJ

"""