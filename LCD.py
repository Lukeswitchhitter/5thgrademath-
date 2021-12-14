e=[]
f=[]
g=[]
A=15
B=19
for i in range(1,100,1):
    c=A*i
    d=B*i
    e.append(c)
    f.append(d)
for i in e:
    for j in f:
        if i == j:
            g.append(i)
print(g[0])           
