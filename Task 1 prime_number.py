import sympy

num1=int(input())
num2=int(input())
prime=[]
oddprime=[]

for num in range(num1, num2 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
        print(num,end=' ')
        prime.append(num)
        
print("\n")

for i in range(0, len(prime), 2):    
    print(prime[i],end=' '); 
    oddprime.append(prime[i])
str1=''.join (str (e) for e in oddprime)

sort= int("".join(sorted([i for i in str(str1)], reverse=True)))
print("\n")
print(sort)
