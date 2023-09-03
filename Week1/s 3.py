#write a python script to enter any number and check it is palindram number or not.

n=int(input('Enter Your Number: '))
temp=n
s=0
while n>0:
    r=n%10
    s=r+(s*10)
    n=n//10
if s==temp:
    print('{} is a palindram number.'.format(temp))
else:
    print('{} is not a palindram number.'.format(temp))