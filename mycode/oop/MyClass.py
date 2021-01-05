#클래스 선언
class MyClass(object):
    #생성자 선언
    def __init__(self):
        #attribute 속성 초기화
        self.num = 100
    # private 속성
        self.__name = 'dooly'
    #method 행위 선언
    def read_number(self):
        return self.num+100

    #부모 클래스가 가진 __str__ 메서드를 재정의
    def __str__(self):
        return f'MyClass의 속성 Num: {str(self.num)}'

    # getter method
    @property
    def name(self):
        return self.__name()


    #setter method
    @name.setter
    def name(self, new_name):
        if len(new_name) == 3:
            self.__name = new_name
        else:
            print('새로운 이름의 길이는 3이어야 합니다.')

# 객체를 생성
myobj1 = MyClass()
print(myobj1, type(myobj1))

# print(myobj1.__name)


myobj1.num = 10
print(myobj1.num)

# setter method 호출
myobj1.name = '길동'

print(myobj1.read_number())

# name 변수는 직접 호출할 수 없다