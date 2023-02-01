# 함수
# 함수정의 ; 이것은 실행이 아님
# 함수 만드는 방법 4가지
# 1. 파라미터o 리턴o
# 2. 파라미터o 리턴x
# 3. 파라미터x 리턴o
# 4. 파라미터x 리턴x


def add(x, y):
    result = x + y
    print(result)
    return


def sub(x, y):
    result = x-y
    print(result)
    return


def mul(x, y):
    result = x * y
    print(result)
    return


def div(x, y):
    result = x // y
    print(result)
    return


def hello():
    print('hello~!')
    return


def hello2():
    msg = 'Hello, Hello'
    return msg


# 함수호출
hello()
print(hello2())

add(1024, 5)
sub(1024, 1000)
mul(512, 2)
div(108, 10)
