x=int(input('angka:'))
if x>=60:
    y1=x//60
    y2=x-(y1*60)
    print(y1,":",y2)
else:
    print(x)
for i in range (1,3):
    print("%3d bb %3d %s"%(i,2*i,"a"))
tup=(8,)