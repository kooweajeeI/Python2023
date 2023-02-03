# 예외처리

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)

except Exception as e:
    print(e)
    print('종료합니다.')
    exit()
finally:                        # finally 무조건 마지막에 수행, 그 이후 종료
    print('계속되나요?')

# 원시적인 예외처리
# if y == 0 :
#     print('y에 0을 넣지 마세요')
#     pass

print('계산 테스트')
try:
    print(f'나눗셈:{div(x, y)}')

# except ZeroDivisionError as e:
#     print('0으로 나누면 안되요')
except Exception as e:          # except 중 제일 마지막에 와야함
    print(e)
finally:
    print('계산을 계속합니다.')


print(f'덧셈:{add(x, y)}')
print(f'곱셈:{mul(x, y)}')
