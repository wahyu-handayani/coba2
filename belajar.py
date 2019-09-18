r=int(input('banyaknya angka:'))
data=[]
for i in range (r): #v
    n=int(input("Enter Integer {}:".format(i+1))) #v
    data.append(n) #v
m=10**(r-1)
for i in range (r):
    y=int(data[i]*m)
    print(y)
    m=m/10

