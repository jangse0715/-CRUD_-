class Member:
    def __init__(self, user_id, password, nickname, age, admin=False):
        self.user_id = user_id
        self.password = password
        self.nickname = nickname
        self.age = age
        self.admin = admin

    def __str__(self):
            return f"닉네임 : {self.nickname} | ID : {self.user_id} | 나이 : {self.age} | 관리자 : {self.admin}"

    def __repr__(self):
            return f" 닉네임 : {self.nickname}, 가입 ID : {self.user_id}"
