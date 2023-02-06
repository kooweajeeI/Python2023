# 주소록 App
# 2023-02-06
# Lee.J.W
# 15. 예외처리 
    # 15-1. 파일 없을 때 발생하는 예외
    # 15-2. 입력 시 / 개수가 다를 때 예외
    # 15-3. 메뉴 입력 시 숫자 아닐 경우 예외
import os       # 운영체제용 모듈

# 2. 클래스 생성
class Contact:
    # 생성자 - 이름, 전화번호, 이메일, 주소
    def __init__(self, name, phone_num, email, addr):
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이    름 : {self.__name}\n'
                   f'전화번호 : {self.__phone_num}\n'
                   f'이 메 일 : {self.__email}\n'
                   f'주    소 : {self.__addr}'
                   )
        return str_res

    # 10. 객체 존재여부 확인
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False

    # 12. 각 멤버변수에 접근하는 함수
    # getName, getPhoneNum, getEmail, getAddr
    def getName(self) -> str:
        return self.__name

    def getPhoneNum(self) -> str:
        return self.__phone_num

    def getEmail(self) -> str:
        return self.__email

    def getAddr(self):
        return self.__addr

# 추가) 화면클리어
def clear_console():
    command = 'clear'   # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'):       # Windows 운영체제라면
        command = 'cls'

    os.system(command)

# 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름/전화번호/이메일/주소) : ').split('/')
    # print(name, phone_num, email, addr)
    # 7. Contact 객체 만들기
    contact = Contact(name, phone_num, email, addr)
    return contact

# 9. 주소록 출력
def get_contacts(list):
    for item in list:
        print(item)
        print('------------------------------')

# 10. 주소록 삭제
def del_contact(list, name):
    count = 0   # 11. 찾는 이름 카운트
    for i, item in enumerate(list):
        if item.isNameExist(name):
            count += 1
            del list[i]  # 리스트 삭제

    if count > 0:  # 11. 메세지 출력

        print('삭제했습니다.')
    else:
        print('삭제할 주소록이 없습니다.')

# 13. 주소록 파일 저장
def save_contacts(list):
    file = open('C:/Source/Python2023/Project/contacts.txt',
                'w', encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')

    file.close()    # 파일 닫아줘야함

# 14. 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/Source/Python2023/Project/contacts.txt',
                'r', encoding='utf-8')
    except Exception as e:
        f = open('C:/Source/Python2023/Project/contacts.txt',
                'w', encoding='utf-8')
        f.close()   # 파일이 없어서 생기는 예외는 파일 생성하고 함수 탈출
        return
        
    while True:
        line = file.readline().replace('\n','')     # 15. 문장 끝 \n 제거
        if not line : break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close()

# 6. 메뉴 표시
def get_menu():
    str_menu = '''주소록앱 v0.5
1. 연락처 추가
2. 연락처 출력
3. 연락처 삭제
4. 앱종료
    '''
    print(str_menu)
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        menu = 0                # 경우에 없는 경우는 무시(영문, 특수문자 등)

    return menu

# 3. 전체 실행
def run():
    contacts = list()   # 정보들을 담기 위한 빈 리스트 생성
    load_contacts(contacts) # 14. 주소록 읽어오기
    # temp = Contact('홍길동', '010-1111-2222', 'gildong@mail.com', '부산시 해운대구')
    # set_contact()
    clear_console()
    while True:
        sel_menu = get_menu()
        
        if sel_menu == 1:      # 8. 연락처 추가
            try:    #15-2 입력 잘못했을 때 예외처리
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공')  # 아무것도 안받는 입력
            except Exception as e:
                print('이름/전화번호/이메일/주소 순으로 똑바로 입력하세요')
            finally:
                clear_console()

        elif sel_menu == 2:    # 9. 연락처 출력
            get_contacts(contacts)
            input('주소록 출력 완료')  # 아무것도 안받는 입력
            clear_console()

        elif sel_menu == 3:    # 10. 연락처 삭제
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()

        elif sel_menu == 4:     # 13. 종료 시 주소록 파일 저장
            save_contacts(contacts)
            clear_console()
            print('저장되었습니다. 앱을 종료합니다.')
            break

        else:
            clear_console()


# 1. 메인 실행영역
if __name__ == '__main__':
    # print('주소록앱 시작합니다.')
    run()
