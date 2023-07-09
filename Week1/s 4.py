#write a python script to enter any numer and check number is armstrong or not

s=0  #sum
n=int(input("Enter Your Number:: ")) #number
temp=n #temporary variable

while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if temp==s:
    print("Armstrong Number")
else:
    print("Not a Armstorng Number")