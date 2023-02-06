# date : 2023-02-06
# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자)

print('1. Hello. \r\nWorld')
print('2.Hello. \nWorld')       # 이걸 권장

print('3.Hello. \n\tWorld')     # t => tab
print('4.Hello. \n\t\bWorld')   # b => backspace

print('5.Hello. \n\'World\'')   # \ => 문자열 내 홑따옴표 출력위함
print('6.Hello. "World"')
print('7.Hello. \"World\"')

print('8.Hello. \\World')       # \\ => \를 문자열에 표현

print('9.Hello\0')             # \0 => 문자열의 끝

# 문자열 포맷팅
# %로 포맷코드를 시작
me = '저'
name = '이재욱'
age = 20
print('%s는 %s입니다. %d대입니다.'%('저', '이재욱', 20))
print('%s는 %s입니다. %d대입니다.'%(me, name, age))

print(f'{254.1122233:.2f}')     # 최신식
print('%7.2f' %254.1122233)      # 구식, 전체자리수.소수자리수



