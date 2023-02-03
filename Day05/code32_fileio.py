# 파일 만들기
# 현재위치 : C:/Source/Python2023
# file = open('C:\DEV\Temp\Bank\sample02.txt', 'w', encoding='utf-8')  # 파일 쓰기로 만듦 # /,\,\\ 다 가능
# 파일 / 폴더 경로 (상대경로 / 절대경로)
file = open('./Day05/sample05.txt', 'w', 'encoding=utf-8')      # Day05에 생성
file = open('./Day05/../Day04/sample06.txt', 'w', 'encoding=utf-8')  # Day04에 생성
file = open('../sample07.txt', 'w', 'encoding=utf-8')       #source에 생성


file.write('안녕하세요~\n')
file.write('두번째 파일이다!\n')
file.write('절대경로에 파일이 생성될겁니다.')


file.close()
print('sample01.txt가 생성되었습니다.')

# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라 언어를 다 표현가능

