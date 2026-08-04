import json
import os

from model.def_model import Member

# 프로그램 시작 시 회원 정보 로딩
if os.path.exists("members.json"):
    with open("members.json", "r", encoding="utf-8") as j:
        # try:
        members_dict = json.load(j)
        # except json.JSONDecodeError:
        #     members = {}
else:
    members_dict = {}

member_list = []
current_user = None  # 현재 로그인한 사람의 정보를 기억해둘 변수


# 메뉴 입력
def get_menu_num():
    print("===================")
    num = int(input("실행할 번호를 입력하세요.   "))
    return num


# 로그인 화면 출력
def print_menu_anyone():
    print("\n===== 회원 관리 프로그램 =====")
    print("0. 프로그램 종료")
    print("1. 회원가입")
    print("2. 로그인")


# 로그인 화면 프로세스  // 두 개의 리턴값
def process_anyone(num):
    match num:
        case 0:
            return True, False  # is_exit, login_result 에 대한 값이 필요
        case 1:
            sign_up()  # 회원가입
            return False, False
        case 2:
            user_id = log_in()  # 로그인
            return False, user_id
        case _:
            print(" \n!!! 올바른 번호를 입력하세오 !!!")


# 회원 메뉴 출력
def print_menu_members():
    print("\n===== 회원 관리 프로그램 =====")
    print("0. 프로그램 종료")
    print("1. 회원목록 조회")
    print("2. 상세 조회")
    print("3. 등록 철회")


# 회원 메뉴 프로세스
def process_members(num, current_member):
    match num:
        case 1:
            get_member_list()  # 회원목록 조회
        case 2:
            get_member_info()  # 등록회원 상세조회
        case 3:
            del_member_info(current_member)  # 회원등록 철회
        case _:
            print(" \n!!! 올바른 번호를 입력하세오 !!!")


# 관리자 여부
def is_admin():
    while True:
        admin = input(" 관리자 계정인가요? Y/N ")
        match admin.lower():
            case "y":
                print("관리자 등급으로 가입되었습니다.")
                return True
            case "n":
                print("일반 회원으로 가입되었습니다.")
                return False
            case _:
                print("잘못된 입력입니다.")


# 객체 등록/ 회원가입
def sign_up():
    print("\n===== 회원가입 =====")
    user_id = input(" 가입 아이디 : ")
    password = input(" 비밀번호 : ")
    nickname = input(" 닉네임 : ")
    age = input(" 나이 : ")
    admin = is_admin()
    m = Member(user_id, password, nickname, age, admin)
    member_list.append(m)
    save_members()
    print("등록되었습니다.")


# 회원 정보 저장
def save_members():
    for m in member_list:
        members_dict[m.user_id] = m.__dict__  # m의 user_id를 키로 하고 m의 딕셔너리를 벨류로 갖는
        # 딕셔너리를 멤버 리스트로부터 뽑아 members_dict에 담겠다.
    with open("members.json", "w", encoding="utf-8") as j:
        json.dump(members_dict, j, ensure_ascii=False, indent=2)  # members_dict 이란 글로벌 변수를 j에 내보내겠다.(저장)


# 로그인
def log_in():
    print("\n===== 로그인 =====")
    user_id = input("아이디: ")
    password = input("비밀번호: ")
    if (user_id in members_dict
            and members_dict[user_id]["password"] == password):
        match members_dict[user_id]["admin"]:
            case True:
                print(" 로그인 성공!\n 관리자 계정입니다.")
            case False:
                print(" 로그인 성공!\n 일반 계정입니다.")
        return user_id

    print("로그인 실패")
    return None


# 계정 등급 정보
def account_degree(i):
    match members_dict[i]["admin"]:
        case True:
            return "관리자"
        case False:
            return "일반 회원"


# 객체 목록/ 회원목록 조회
def get_member_list():
    print("\n가입한 회원의 목록을 출력합니다.")
    if members_dict == {}:
        print("가입된 회원이 없습니다. 회원을 등록해주세요.")
    for i in members_dict:
        print(f"회원 ID : {i} | 닉네임 : {members_dict[i]["nickname"]}")


# 상세조회/ 등록회원 상세조회
def get_member_info():
    print("\n===== 회원정보 상세조회 =====")
    i = input("조회할 회원 아이디를 입력하세요.\n")
    if i not in members_dict:
        print("존재하지 않는 회원입니다.")
    else:
        print(f"'{members_dict[i]['nickname']}'님의 정보를 조회합니다.")
        print(
            f"회원 ID : {i} | 닉네임 : {members_dict[i]["nickname"]} | 나이 : {members_dict[i]["age"]} | 계정등급 : {account_degree(i)}")


# 권한 확인
def confirm_admin(current_user):
    if not members_dict[current_user]["admin"]:
        print("해당 권한이 없는 계정입니다.")
        return


# 삭제/ 회원등록 철회
def del_member_info(current_user):
    confirm_admin(current_user)
    print("\n===== 등록 철회 =====")
    while True:
        i = input("등록을 철회할 회원의 아이디를 입력하세요.\n")

        if i not in members_dict:
            print("존재하지 않는 회원입니다.")
            continue
        # 등록 철회 요청 재확인 메세지
        is_real = True
        while True:
            answer = input(f"\n정말로 '{members_dict[i]['nickname']}'님의 가입을 철회하시겠습니까? Y/N\n")
            match answer.lower():
                case "y":
                    break
                case "n":
                    print("취소했습니다.")
                    is_real = False
                    break
                case _:
                    print("잘못된 입력입니다.")

        if not is_real:
            continue
        else:
            print(f"'{members_dict[i]['nickname']}'님의 정보가 삭제되었습니다.")
            del members_dict[i]
            save_members()
            break

# 프로그램 시작
def program_start():
    while True:
        try:
            is_logged_in = False
            while True:
                # 로그인 화면
                if not is_logged_in:
                    print_menu_anyone()
                    num = get_menu_num()
                    is_exit, login_result = process_anyone(num)
                    if is_exit:
                        break
                    if login_result:
                        current_user = login_result
                        is_logged_in = True
                # 회원 화면
                if is_logged_in:
                    print_menu_members()
                    num = get_menu_num()
                    process_members(num, current_user)
                    if num == 0: break

        except Exception as e:  # 예외가 나온다면 잡아서 원래 흐름으로 돌아가고 싶다.
            print("[예외 발생]", e)
            print("그치만 멈추지 않을 거에오")
