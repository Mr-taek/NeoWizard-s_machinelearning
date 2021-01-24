import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2],[3,4],[5,6]])

c=np.dot(a,b)

print(c)

a=np.array([[1,2,3,4],[2,3,4,5]])
b=np.array([[1,2,3,4],[2,3,4,5]])

c=np.add(a,b)

print(c)


# NUMPY 2 , 전치행렬

import numpy as np

#a=np.array([[1,2],[3,4],[5,6]])
#b=a.T
#print(b)

#iterator

a=np.array([[1,2,3,4],[2,3,4,5]])

it=np.nditer(a,flags=['multi_index'], op_flags=['readwrite']) #1.  a의 첫 원소 1을 가르키고 있는 상태.

while not it.finished:                                        #3. iterator는 자체적으로 다음 인덱스를 자동으로 불러오지 않기 때문에 항상 while 문과 셋으로 사용된다.
    idx=it.multi_index
                                                            #4. iterator은 행 단위로 증가한다.
    it.iternext() 

print(it)