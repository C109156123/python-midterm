
a=input("輸入一組四位數字為:")
list1=list(map(int,a))
b=((list1[0]+7)%10)
c=((list1[1]+7)%10)
d=((list1[2]+7)%10)
e=((list1[3]+7)%10)
print(str(d)+str(e)+str(b)+str(c))
