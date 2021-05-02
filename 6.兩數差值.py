
a=""
n=input("輸入值為:").split(",")
n.sort()
m = sorted(n, reverse = True)
minn=int(a.join(n))
maxx=int(a.join(m))
print("最大值數列與最小值數列差值為:"+str(maxx-minn))
