
a=int(input("組數為:"))
for i in range(a):
    b,c=map(int,input("第"+str(i+1)+"組:").split())
    d=b*250+c*175
    print("第"+str(i+1)+"組應收費用:"+str(d))