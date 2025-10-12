from jwt_token import create_token, access_token, userdata

# 간단한 유저 DB
users = {}

class UserData:
    def __init__(self):
        self.token = None
        self.id = None

    # 회원가입
    def signup(self):
        user_id = input("아이디를 입력하세요: ")
        if user_id in users:
            print("이미 존재하는 아이디입니다.")
            return False
        password = input("비밀번호를 입력하세요: ")
        users[user_id] = password
        print("회원가입 성공!")
        return True

    # 로그인
    def login(self):
        user_id = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        if users.get(user_id) != password:
            print("로그인 실패! 아이디/비밀번호 확인 필요")
            return None

        self.id = user_id
        self.token = create_token(user_id)
        print("로그인 성공! 발급된 토큰:", self.token)
        return self.token

    # 의존성 주입
    def depend_func(self, func):
        def wrapper():
            # 토큰 없으면 로그인 다시
            if not self.token:
                print("토큰 없음 → 로그인 필요")
                self.login()

            # 토큰 검증
            user_id = access_token(self.token)
            if not user_id:
                print("토큰 검증 실패 → 재로그인 필요")
                self.login()
                return func()
            else:
                return func()
        return wrapper

    # 보호된 페이지
    @property
    def protected_page(self):
        @self.depend_func
        def inner():
            print(f"환영합니다 {self.id}님! 보호된 페이지에 접근했습니다.")
        return inner()


if __name__ == "__main__":
    user = UserData()
    while True:
        print("\n1) 회원가입\n2) 로그인\n3) 보호된 페이지\n4) 종료")
        choice = input("선택: ")

        if choice == "1":
            user.signup()
        elif choice == "2":
            user.login()
        elif choice == "3":
            user.protected_page
        elif choice == "4":
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")