# date : 2023-02-02
# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'
    def __init__(self, name='홍길동', height='170', gender='male') -> None:
        self.name = name
        self.height = height
        self.gender = gender

    # def __init__(self, name, height, gender) -> None:
    #     self.name = name
    #     self.height = height
    #     self.gender = gender

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자 외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력: 이름은 {self.name}, 성별은 {self.gender}'


# jaewook = Person()  # 객체생성    #객체를 instance라고 함
# jaewook.name = '이재욱'
# jaewook.height = '123'
# jaewook.gender = 'male'
# jaewook.blood_type = 'A'

# print(f'{jaewook.name}의 혈액형은 {jaewook.blood_type}입니다.')

# jaewook.walk()
# jaewook.run('Fast')
# jaewook.stop()

# 1. 초기화 후 객체생성
# hong = Person()
# hong.run('Slow')

print('------------------------------------------------------------')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 160, '여자')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)