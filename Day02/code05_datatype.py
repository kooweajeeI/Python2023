# date : 2023-01-31
# 자료형
# None : 값이 없는 값
None # 컴퓨터왈 난몰라
print(None)
print(0 == None)
print('' == None)

# 숫자형 int, float
val = 3
print(val)
print(type(val))

val = 3.14
print(type(val))

val = 0b1010
print(val)
print(type(val))

val = 12.41242141414
print(type(val))

val = 4_520_000 # _ : 사람이 구분하기 쉽게 쉼표역할 (예)4,520,000
print(val)

val = 3_909.99
print(val)

# 문자열형 str
val = 'Hello!'
print(type(val))

val = 'Life is short, You need Python.'
print(val)
print(type(val))

# 탈출문자 Escape Sequence
val = 'Hell\nWorld' # \n : Enter
print(val)

val = 'Hell\tWorld' # \t : Tab
print(val)

val = 'Hell\t\bWorld' # \b : Backspace
print(val)

val = "Hi, I'm 'Jaewook'"
print(val)
val = 'Hi, I\'m \'Jaewook\''
print(val)

# 홀따옴표(쌍따옴표) 3개면 여러 줄 문자열
# 파이썬에서는 홀따, 쌍따 구분없음
val = '''Life is short,
You need Python'''
print(val)

# Boolean형 (True, False)
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 1)
print(1 + 1 == 2)

# 거짓이라는 False값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

# 1은 True 0은 False, 1 이상의 값들은 True로 간주(0이 아니면 True)
print(bool(1))
print(bool(0))
print(bool(3))