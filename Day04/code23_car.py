# 자동차 클래스
import code
class Car:
    __number = '102주 8274'  # 캡슐화 : __

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number
        

    def __init__(self) -> None:
        print('__init__')

    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls)     # 부모클래스(상속)

    def __str__(self) -> str:
        return f'내 차 번호 : {self.__number}'


yourcar = Car()                    
yourcar.__number = ('333삼 3333')     # 안통함 외부에서는 멤버변수에 접근불가
print(yourcar)
yourcar.set_number('555오 5555')    # 이건 통함
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는요, 번호가 {mycar.get_number()}이에요.')

mycar.number = '123사 5678'
print(mycar)
