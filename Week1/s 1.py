#write a python script to Enter any Number and check it is prime or not.

n=int(input('Enter Any Number:: '))
c=0 #it called count.it is used to define how many times the number is divided.
i=1 
for i in range(i,n+1):
   if n%i==0:
     c+=1
   i+=1
if c==2:
   print('It is prime Number')
else:
   print('It is not a prime Number')