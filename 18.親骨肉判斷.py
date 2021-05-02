
a,b,c=input().split()
if a=="O" and b=="O" and c=="O":
    print("Yes")
elif a=="A" and b=="O" and(c=="A"or"O"):
    print("Yes")
elif a=="B" and b=="A" and(c=="B"or"O"):
    print("Yes")
elif a=="O" and b=="AB" and(c=="A"or"B"):
    print("Yes")
elif a=="A" and b=="A" and(c=="A"or"O"):
    print("Yes")
elif a=="A" and b=="B":
    print("Yes")
elif a=="A" and b=="AB" and(c=="A"or"B"or"AB"):
    print("Yes")
elif a=="B" and b=="B" and(c=="B"or"O"):
    print("Yes")
elif a=="B" and b=="AB" and(c=="A"or"B"or"AB"):
    print("Yes")
elif a=="AB" and b=="AB" and(c=="A"or"B"or"AB"):
    print("Yes")
else:
    print("impossible")