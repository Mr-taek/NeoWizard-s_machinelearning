even_number = []
for data in range(10):
    if data%2==0:
        even_number.append(data)

print(even_number)

# quiz:  짝수가 출력되는 위 함수를 list comprehension으로 구현하라.

even_number=[]

x=[y for y in range(0,10,2)]
print(x)

raw=[[1,10], [2,15], [3,20], [4,25], [5,30]]

all=[x for x in raw]
x=[x[0] for x in raw]
y=[z[1] for z in raw]

print(x,y)