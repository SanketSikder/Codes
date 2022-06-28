import numpy as np
"""
new_matrix = np.array(([[[1,2,3],[4,5,6],[7,8,9]]]))
print(new_matrix)
print(new_matrix.ndim)
print(new_matrix.size)
print(np.linspace(start=0,stop=20,num=10,dtype=float,endpoint=False,retstep=True))
print(np.eye(3,3))
a=np.arange(9).reshape(3,3)
print(a)
#flatten
b=a.flatten()
print(b)
b[0]=10
print(b)
print(a)
#Ravel
c=a.ravel()
print(c)
c[0]=10
print(c)
print(a)

x=np.arange(6).reshape(2,3)
y=np.arange(6,12).reshape(2,3)
print(x)
print(y)
print(np.concatenate((x,y),axis=0))
print(np.concatenate((x,y),axis=1))
print(np.concatenate((x,y),axis=None))
print(np.vstack((x,y)))
print(np.hstack((x,y)))
"""
#insert
d=np.arange(4).reshape(2,2)
e=np.insert(d,1,(5,6),axis=0)
print (e)
e=np.insert(d,1,(5),axis=1)
print(e)
#linear equations
#x+2y=10
#3x+3y=18
a=np.array([[1,2],[3,3]])
b=np.array([10,18])
res=np.linalg.solve(a,b)
print(res)