import json
import os

from model.def_model import Member

# 프로그램 시작 시 회원 정보 로딩
if os.path.exists("members.json"):
    with open("members.json", "r") as j:
        # try:
        members_dict = json.load(j)
        # except json.JSONDecodeError:
        #     members = {}
else:
    members_dict = {}

member_list = []
current_member = None  # 현재 로그인한 사람의 정보를 기억해둘 변수


# 프로그램 출력
def print_program():
    print("\n===== 회원 관리 프로그램 =====")


# 로그인 화면 출력
def print_menu_anyone():
    print("0. 프로그램 종료")
    print("1. 회원가입")
    print("2. 로그인")


# 가입자 전용 메뉴 출력
def print_menu_members():
    print("0. 프로그램 종료")
    print("1. 회원목록 조회")
    print("2. 상세 조회")
    print("3. 등록 철회")


# 메뉴 입력
def get_menu_num():
    print("===================")
    num = input("실행할 번호를 입력하세요.   ")
    return num


# 프로세싱
def process_anyone(num_menu):
    match num_menu:
        case "0":
            return True, False  # is_exit, is_logged_in
        case "1":
            sign_up()  # 회원가입
            return False, False
        case "2":
            user_id = log_in()  # 로그인
            return False, user_id
        case _:
            print(" \n!!! 올바른 번호를 입력하세오 !!!")


def process_members(num_menu, current_member):
    match num_menu:
        case "0":
            return True
        case "1":
            get_member_list()  # 회원목록 조회
        case "2":
            get_member_info()  # 등록회원 상세조회
        case "3":
            del_member_info(current_member)  # 회원등록 철회
        case _:
            print(" \n!!! 올바른 번호를 입력하세오 !!!")


# 관리자 여부
def is_admin():
    while True:
        admin = input(" 관리자 계정인가요? Y/N ")
        match admin.lower():
            case "y":
                return True
            case "n":
                return False
            case _:
                print("잘못된 입력입니다.")


# 회원 정보 저장
def save_members():
    for m in member_list:
        members_dict[m.id] = m.__dict__

    with open("members.json", "w") as j:  # members.json은 파일명.확장자 / w는 쓰기모드 / j는 파일호출 변수
        json.dump(members_dict, j)  # 'members_dict'의 정보(딕셔너리)를 JSON 형식으로 변환해서 j라는 파일(members.json)에 저장


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
        save_members()
        print("등록되었습니다.")
        break


# 로그인
def log_in():
    print("\n===== 로그인 =====")
    user_id = input("아이디: ")
    password = input("비밀번호: ")
    if (user_id in members_dict
            and members_dict[user_id]["password"] == password):
        print("로그인 성공!")
        return user_id

    print("로그인 실패")
    return None


# 객체 목록/ 회원목록 조회
def get_member_list():
    print("\n가입한 회원들의 목록을 출력합니다.")
    if members_dict == {}:
        print("가입된 회원이 없습니다. 회원을 등록해주세요.")
    for i in members_dict:
        print(f"회원 ID : {i} | 닉네임 : {members_dict[i]["nickname"]}")


# 상세조회/ 등록회원 상세조회
def get_member_info():
    print("\n===== 등록회원 상세조회 =====")
    i = input("조회할 회원의 아이디를 입력하세요.\n")
    print(f"'{members_dict[i]['nickname']}'님의 정보를 조회합니다.")
    print(f"회원 ID : {i} | 닉네임 : {members_dict[i]["nickname"]} | 나이 : {members_dict[i]["age"]} | 관리자 : {members_dict[i]["admin"]}")


# 삭제/ 회원등록 철회
def del_member_info(current_member):
    if not members_dict[current_member]["admin"]:
        print("권한이 없습니다.")
        return

    print("\n===== 등록 철회 =====")
    while True:
        target_id = input("등록을 철회할 회원의 아이디를 입력하세요.\n")

        if target_id not in members_dict:
            print("존재하지 않는 회원입니다.")
            continue

        is_real = True
        while True:
            answer = input(f"\n정말로 '{members_dict[target_id]['nickname']}'님의 가입을 철회하시겠습니까? Y/N\n")
            match answer.lower():
                case "y":
                    break
                case "n":
                    print("취소했습니다.")
                    is_real = False
                    break
                case _:
                    print("잘못된 입력입니다.")

        if is_real == False:
            continue
        else:
            print(f"'{members_dict[target_id]['nickname']}'님의 정보가 삭제되었습니다.")
            del members_dict[target_id]
            save_members()
            break
