# Q1
x, y = map(int, input().split(','))
res = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(i*j)
    res.append(row)
print(res)

# Q2
items = input().split(',')
items.sort()
print(','.join(items))

# Q3
words = input().split()
print(' '.join(sorted(set(words))))

# Q4
l = []
for i in range(1000,3001):
    s = str(i)
    if all(int(ch)%2==0 for ch in s):
        l.append(s)
print(','.join(l))

# Q5
s = input()
c=d=0
for ch in s:
    if ch.isalpha(): c+=1
    elif ch.isdigit(): d+=1
print("LETTERS", c)
print("DIGITS", d)

# Q6
s = input()
u=l=0
for ch in s:
    if ch.isupper(): u+=1
    elif ch.islower(): l+=1
print("UPPER CASE", u)
print("LOWER CASE", l)

# Q7
total = 0
while True:
    s = input()
    if not s: break
    if s[0] == 'D': total += int(s[2:])
    elif s[0] == 'W': total -= int(s[2:])
print(total)

# Q8
import re
lst = input().split(',')
for pwd in lst:
    if 6<=len(pwd)<=12 and re.search("[a-z]", pwd) and re.search("[A-Z]", pwd) and re.search("[0-9]", pwd) and re.search("[$#@]", pwd):
        print(pwd)

# Q9
lst = []
while True:
    s = input()
    if not s: break
    lst.append(tuple(s.split(',')))
lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(lst)

# Q10
x=y=0
while True:
    s = input()
    if not s: break
    dir, steps = s.split()
    steps=int(steps)
    if dir=='UP': y+=steps
    elif dir=='DOWN': y-=steps
    elif dir=='LEFT': x-=steps
    elif dir=='RIGHT': x+=steps
dist = int(round(math.sqrt(x**2 + y**2)))
print(dist)

# Q11
s = input()
res=""
i=0
while i<len(s):
    count=1
    while i+1<len(s) and s[i]==s[i+1]:
        count+=1
        i+=1
    res+=s[i]+str(count)
    i+=1
print(res)

# Q12
s=input()
letters = []
numbers = []
buf = ""
for ch in s:
    if ch.isalpha():
        if buf:
            numbers.append(int(buf))
            buf = ""
        letters.append(ch)
    elif ch.isdigit():
        buf += ch
if buf:
    numbers.append(int(buf))
for i in range(len(letters)-1):
    if numbers[i]==9:
        print(letters[i]+","+letters[i+1])

# Q13
s=input()
c=s.count('1')
print(c*(c-1)//2)

# Q14
curr = list(map(int, input().split(',')))
money = int(input())
curr.sort(reverse=True)
for c in curr:
    if money>=c:
        cnt=money//c
        money-=cnt*c
        print(f"{c}-{cnt}")

# Q15
import math
n,m=map(int,input().split())
print(math.comb(n-m+1,m))

# Q16
scoreA=scoreB=0
while scoreA<5 and scoreB<5:
    a,b=input().split()
    if a==b: print("DRAW")
    elif (a,b) in [("Stone","Scissor"),("Paper","Stone"),("Scissor","Paper")]:
        scoreA+=1
        print("Player A wins")
    else:
        scoreB+=1
        print("Player B wins")

# Q17
s=input()
if s.count('@')==1 and all(ch.islower() or ch.isdigit() or ch in ['.','_','@'] for ch in s):
    print("Valid")
else:
    print("Invalid")

# Q18.1
n=int(input())
c=1
for i in range(1,n+1):
    for j in range(i):
        print(c,end='')
        c+=1
        if j!=i-1: print("*",end='')
    print()

# Q18.2
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)

# Q18.3
n=int(input())
c=1
for i in range(1,n+1):
    for j in range(i):
        print(c,end='')
        c+=1
        if j!=i-1: print("*")
    print()
for i in range(n-1,0,-1):
    c-=i
    for j in range(i):
        print(c,end='')
        c+=1
        if j!=i-1: print("*")
    c-=i
    print()

# Q18.4
n=int(input())
for i in range(n):
    for j in range(n):
        if (i in [0,n-1]) or (j==n//2):
            print('*')
        else:
            print(' ')
    print()

# Q18.5
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print(1)
        else:
            print(0)
    print()

# Q19
t=int(input())
s=input()
k=int(input())
for i in range(k):
    if t==1:
        s=s[1:]+s[0]
    else:
        s=s[-1]+s[:-1]
    print(s)

# Q20
ideal={'Sugar level':15,'Blood pressure':32,'Heartbeat rate':71,'weight':65,'fat percentage':10}
actual={}
for k in ideal:
    actual[k]=int(input())
diff={k:actual[k]-ideal[k] for k in ideal}
print(diff)
for k in diff:
    if diff[k]>0:
        print(f"{k} {diff[k]}\n{k} is {diff[k]} more than the ideal value")
    else:
        print(f"{k} {diff[k]}\n{k} is {-diff[k]} less than the ideal value")

# Q21
n=input()
p=len(n)
if sum(int(i)**p for i in n)==int(n):
    print("Armstrong number")
else:
    print("Not Armstrong")

# Q22
n=int(input())
b=""
while n:
    b=str(n%2)+b
    n//=2
print(b)

# Q23
n=int(input())
sum_div=sum(i for i in range(1,n) if n%i==0)
if sum_div==n:
    print("Perfect number")
else:
    print("Not perfect")
