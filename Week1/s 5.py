#write a python script to enter any string and count vowel.

a=input("Enter Any String:: ")
c=0  #count
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        c+=1
    elif(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        c+=1
print("number of vowels: ",c)