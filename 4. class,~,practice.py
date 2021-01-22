# example for 맴버변수, 클래스 메소드.
class Person:
        count=0     # class variable
        def __init__(self, name):       
            self.name=name
            Person.count+=1     # 맴버변수 count는 person class가 호출될 때마다 1씩 증가한다.    
            print(self.name)

        def work(self, company):
            print(self.name+company)

        def sleep(self):
            print(self.name+" sleep")
        
        @classmethod        # 아래 method는 class method임을 표시. 이렇게 선언된 함수는 Person.getcount() 로서 호출이 가능해진다.
        def getcount(cls):
            return cls.count

    # person instance 객체 2개 생성.
#obj1=Person("park")
#obj2=Person("LEE")
#obj1.work("abocado") # obj1의 work를 실행           
#obj2.sleep()         # obj2의 sleep 실행

#print(obj1.name,obj2.name)
#print(Person.getcount())    # 앞에 두개의 인스턴스가 두개 생성되었으므로 2가 나오고
#print(Person.work()) # 객체로 만들어야 실행 가능한 Person의 함수이다.
#print(Person.count)


# public -> private 예제
class pri:
    def __init__(self,name1,name2):
        self.name1=name1
        self.__name2=name2  # private variable.
    
    def getnames(self):
        self.__prinnames()  # prinnames는 private이므로 같은 class내에서만 접근가능, 따라서 외부접근이 안되니 getnames()메소드를 이용해 prinnames를 호출한다.
        return self.name1,self.__name2  # name2가 private이므로 외부에선 접근 불가, 그래서 getnames를 이용해 접근하여 출력시킨다.

    def __prinnames(self):
        print(self.name1, self.__name2)

obj=pri("park","kim")

#print(obj.name1)
#print(obj.getnames(),type(obj.getnames()))
#print(obj.__prinnames())    # private이므로 접근불가
#print(obj.__name2)          # private이므로 접근불가

# 같은 이름의 외부함수와 class의 내부함수 구별
def print_name(name):
    print(name)
class same:
    # init은 초기화 할 것이 없기 때문에 생략.

    def print_name(self,name):
        print("[same]"+name)
    def call_test(self):
        print_name("KIM")

        self.print_name("KIM")  # 이렇게 self를 써줌으로서 class의 내부 함수와 class 밖에 있는 같은 이름의 함수를 구별해준다.

obj= same()
print_name("LEE")
obj.print_name("LEE")
obj.call_test()