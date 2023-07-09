#write a python script to enter any string and print only part of string.

name=input('enter string: ')
a=input('start character:')  #starting character
b=input('Ending character:') #ending character
#using .index we can easily perform this programe
x=name.index(a)  #starting character index
y=name.index(b)    #ending character index
print('New string is : ',name[x:y+1])