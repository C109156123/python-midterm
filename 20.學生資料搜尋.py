
num=["123","456","789","321","654"]
name=["Tom","Cat","Nana","Lim","Won"]
d=["DTGD","CSIE","ASIE","DBA","FDD"]
n=input("輸入查詢學號為:")
a=num.index(n)
b=num[a]
if n==b:
    print("學生資料為:"+str(num[a]+name[a]+d[a]))
else:
    print("查無此號碼")