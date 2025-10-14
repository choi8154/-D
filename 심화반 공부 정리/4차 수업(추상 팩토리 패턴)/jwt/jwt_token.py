from datetime import datetime, timedelta
import hashlib, json, hmac
from base64_encode import base64_encode

userdata = []
secret_key = b"sldkfjsienfj"

#토큰 발급 함수
def create_token(sub:str, name)->str:
    iat = datetime.utcnow()
    exp = str(iat + timedelta(minutes=60))

    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": sub, "name":name, "exp":exp}

    header_b64 = base64_encode(json.dumps(header,separators=(",",":")))
    payload_b64 = base64_encode(json.dumps(payload, separators=(",",":")))

    # 디버깅
    # print("="*50)
    # print("header_b64 : ", header_b64, "type : ", type(header_b64))
    # print("header_b64 : ", payload_b64, "type : ", type(payload_b64))
    # print("="*50)

    # 서명 헤더, 페이로드 bytes로 변환해서 sha인코딩 가능하도록 변환
    signature_input = f"{header_b64}.{payload_b64}".encode()

    # HMAC(Hash-based Message Authentication Code)객체 생성
    signature = hmac.new(secret_key, signature_input, hashlib.sha256).digest()
    signature_b64 = base64_encode(signature)

    # 유저 정보 저장하기
    userdata.append({"sub": sub,"name": name, "exp":exp, "signature": signature}) 
    token = f"{header_b64}.{payload_b64}.{signature_b64}"

    # print("토큰 : ",token)
    return token
