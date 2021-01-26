import numpy as np

q=np.array([[[4,2,1,2],[1,2,3,4],[3,4,5,6]],[[3,4,1,2],[10,11,2,40],[30,40,11,21]]])

x=np.max(q,axis=1)
y=np.max(q,axis=0)
x1=np.argmax(q,axis=1)
y1=np.argmax(q,axis=0)
print(q)
#print(x)
#print(x1)
print(y)
print(y1)