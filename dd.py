import numpy as np

a=np.array([[1,2,3],[3,4,5]])

row=np.array([7,8,9]) # 그냥 이대로만 두면 (3,1)의 벡터가 되므로 행열로 만들어 줘야 한다.
row=row.reshape(1,3)
print(row)

colum=np.array([1000,2000]).reshape(2,1)

b=np.concatenate((a,row),axis=0)
d=np.concatenate((a,colum),axis=0)

print(b)
print(d)