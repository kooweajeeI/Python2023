# date : 2023-02-01

name = '재욱'
state = '아픔'

if name == '재욱':
    print('진료실에서 담당의사를 만납니다.')
    if state == '아픔':
        print('선생님, 아파요~.')
        print('어디가 어떻게 아프십니까?')
    else:
        print('어디가 아프십니까?')
        print('안 아픈데요?')
        print('그럼 왜 오셨어요?')

elif name == '채원':
    print('주사실로 갑니다.')
    print('엉덩이 내리세요~')

else:
    print('조용히 기다립니다.')
