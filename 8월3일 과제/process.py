from unittest import case

from model.def_model import Member

member_list = []


# 프로그램 출력
def print_program():
    print("\n===== 회원 관리 프로그램 =====")


# 메뉴 출력
def print_menu():
    print("0. 프로그램 종료")
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 회원목록 조회")
    print("4. 상세 조회")
    print("5. 등록 철회")


# 메뉴 입력
def get_menu_num():
    print("===================")
    num = input("실행할 번호를 입력하세요.   ")
    return num


# 프로세싱
def working_process(num_menu):
    match num_menu:
        case "0":
            return True
        case "1":
            sign_up()  # 회원가입
        case "2":
            log_in()  # 로그인
        case "3":
            get_member_list()  # 회원목록 조회
        case "4":
            get_member_info()  # 등록회원 상세조회
        case "5":
            del_member_info()  # 회원등록 철회
        case _:
            print(" \n!!! 올바른 번호를 입력하세오 !!!")


# 관리자 여부
def is_admin():
    while True:
        admin = input(" 관리자 계정인가요? Y/N ")
        match admin.lower():
            case "y":
                return "관리자"
            case "n":
                return "일반 회원"
            case _:
                print("잘못된 입력입니다.")


# 객체 등록/ 회원가입
def sign_up():
    while True:
        print("\n===== 회원가입 =====")
        id = input(" 가입 아이디 : ")
        password = input(" 비밀번호 : ")
        nickname = input(" 닉네임 : ")
        age = input(" 나이 : ")
        admin = is_admin()
        m = Member(id, password, nickname, age, admin)
        member_list.append(m)
        if admin:
            print(f"'{admin}'(으)로 등록되었습니다.")
            break


# 로그인
def log_in():
    print("\n===== 로그인 =====")
    print("\n===== (미구현) =====")


# 객체 목록/ 회원목록 조회
def get_member_list():
    print("\n가입한 회원들의 목록을 출력합니다.")
    if member_list == []:
        print("가입된 회원이 없습니다. 회원을 등록해주세요.")
    for idx, i in enumerate(member_list):
        print(f"회원번호: {idx} | 닉네임: {i.nickname} | 가입 ID: {i.id}")


# 상세조회/ 등록회원 상세조회
def get_member_info():
    print("\n===== 등록회원 상세조회 =====")
    n = int(input("조회할 객체 번호를 입력하세요.   "))
    m = member_list[n]
    print(f"\n'{m.nickname}'님의 정보를 불러옵니다.")
    print(m)   # str 호출


# 삭제/ 회원등록 철회
def del_member_info():
    print("\n===== 등록 철회 =====")
    while True:
        n = int(input("등록을 철회할 회원의 번호를 입력하세요.   "))
        m = member_list[n]
        is_real = False
        while True:
            answer = input(f"\n정말로 '{m.nickname}'님의 가입을 철회하시겠습니까? Y/N\n")
            match answer.lower():
                case "y":
                    break
                case "n":
                    print(f"취소했습니다.")
                    is_real = True
                    break
                case _:
                    print("잘못된 입력입니다.")
        if is_real:
            continue
        else:
            print(f"'{m.nickname}'님의 정보가 삭제되었습니다.")
            del member_list[n]
            break
