#for loop
'''
for i in reversed(range(1,11)):
    print(i)
'''
'''
2 X 1= 2
2 X 2= 4
'''
'''
for i in range(1,11):
    print(f"2 X {i} = {2*i}")
'''
'''
result = 0
for i in range(1,11):
    result += i
print(result)
'''

#find the sum of digits of number
#find the reverse of number
#check wether number is armstrong or not
'''    
n = int(input("Enter Number:"))
n1=n
result = 0
for i in range(len(str(n))):
    rem = n%10
    result+= rem**3
    n = n//10

if result == n1:
    print("Armstrong")
else:
    print("Not an Armstrong")
'''
'''
#fibonacci Series
#0 1 1 2 3 5 8 13 21
f=0
s=1
print(f)
print(s)
for i in range(8):
    t = f+s
    print(t)
    f,s = s,t
'''
'''
#break
for i in range(1,1000001):
    print(i)
    if i==100:
        break

'''
'''
#continue
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
'''
#homework
#->check wether number is prime or not
