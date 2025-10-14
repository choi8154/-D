import base64
from jwt_token import userdata, secret_key, create_token
from datetime import datetime
import hmac, hashlib, json
from base64_encode import base64_decode


def access_token(token: str):

    header_b64, payload_b64, signature_b64 = token.split(".")

# ===============payload 디코딩===============
    try:
        payload_json = base64_decode(payload_b64).decode("utf-8")
        payload = json.loads(payload_json)
    except Exception:
        raise ValueError("올바르지 않은 형식의 payload")

# ===============payload 검사===============
    sub = payload.get("sub")
    exp_str = payload.get("exp")

    if sub is None or exp_str is None:
        raise ValueError("payload에 정보가 유실됨")

    # print("=" * 50)
    # print(f"아이디 : {sub}\n유효기간 : {exp_str}")
    # print("=" * 50)

# ===============유효기간 확인===============
    try:
        exp_dt = datetime.fromisoformat(exp_str)
    except Exception:
        raise ValueError("exp 값이 올바른 datetime 형식이 아님")

    # 만료 확인
    if exp_dt < datetime.utcnow():
        raise ValueError("토큰 기간 만료됨")

    # userdata에서 해당 sub 찾기
    data = next((d for d in userdata if d.get("sub") == sub), None)
    if data is None:
        raise ValueError("해당 사용자의 토큰 데이터가 존재하지 않음")

# ===============서명 확인===============

    # 저장된 서명 꺼내기
    signature = data.get("signature")
    if signature is None:
        raise ValueError("서명이 유실됨")

    # 새로운 서명 생성 (검증용)
    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    computed_sig = hmac.new(secret_key, signing_input, hashlib.sha256).digest()

    # 저장된 서명 형식 맞추기
    if isinstance(signature, str):
        try:
            signature_bytes = base64_decode(signature)
        except Exception:
            try:
                signature_bytes = bytes.fromhex(signature)
            except Exception:
                raise ValueError("저장된 서명의 형식을 해석할 수 없음")
    elif isinstance(signature, (bytes, bytearray)):
        signature_bytes = bytes(signature)
    else:
        raise ValueError("서명 형식이 잘못됨")

    # 서명 검증
    if not hmac.compare_digest(computed_sig, signature_bytes):
        raise ValueError("서명이 일치하지 않음")

    return sub



token = create_token("user123", "람")
try:
    subject = access_token(token)
    print("유효한 토큰, sub:", subject)
except Exception as e:
    print("토큰 검증 실패:", e)