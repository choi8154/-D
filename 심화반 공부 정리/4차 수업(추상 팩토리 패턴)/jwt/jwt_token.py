from datetime import datetime, timedelta
from random import randint
import hashlib

userdata = []

#토큰 발급 함수
def create_token(id):
    secret_key = "sldkfjsienfj"
    iat = datetime.utcnow()
    exp = iat + timedelta(minutes=60)

    # 서명 만들기
    signature = "".join([hashlib.sha256(str(d).encode()).hexdigest() for d in [id, secret_key, exp]]) 

    # 유저 정보 저장하기
    userdata.append({"id": str(id), "exp":exp, "signature": signature}) 
    token = ".".join(map(str, [id, exp ,signature])) # 
    # print("토큰 : ",token)
    return token

#토큰 엑세스 함수
def access_token(token):
    try :
        id, exp1, exp2, signature = [i for i in token.split(".")]
        exp = ".".join([exp1, exp2])
        print("id : ", id, "\nexp :", exp, "\nsignature :",signature)
        print()
        print(userdata)

        # 해당하는 id값이 없으면
        if id not in [data["id"] for data in userdata]:
            # print(id)
            # print([data["id"] for data in userdata])
            raise ValueError("토큰 값이 유효하지 않음")
        
        # id값이 있으면 id를 반환
        data = next(d for d in userdata if d["id"] == id)

        # 토큰 유효기간 확인
        if datetime.fromisoformat(exp) < datetime.utcnow():
            raise ValueError("토큰이 만료됨")
        
        # 토큰 서명 확인
        if data["signature"] != signature:
            raise ValueError("서명이 유효하지 않음")
        return id
    except Exception as e :
        print("오류는  : ", e)


if __name__ == "__main__":
    token = create_token(123)
    result = access_token(token)
    print(result)