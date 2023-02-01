# 구구단 프로그램
for x in range(2, 10):
    print (f'============== {x}단 시작 ==============')
    for y in range(1, 10):
        print(f'{x} x {y} = {x*y:>2}', end=' / ')       # :>2 두 자리로 오른쪽 정렬
    print(' ')
