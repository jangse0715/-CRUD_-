class Member:
    def __init__(self, id, password, nickname, age, admin=False):
        self.id = id
        self.password = password
        self.nickname = nickname
        self.age = age
        self.admin = admin

    def __str__(self):
            return f"닉네임 : {self.nickname} | ID : {self.id} | 나이 : {self.age} | 관리자 : {self.admin}"

    def __repr__(self):
            return f" 닉네임 : {self.nickname}, 가입 ID : {self.id}"
