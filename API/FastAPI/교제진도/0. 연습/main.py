# main.py
import time
from fastapi import FastAPI, Depends, APIRouter, HTTPException, Header, status
from datetime import datetime, timedelta, timezone
import uvicorn
from typing import Optional
from jwt import encode, decode
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError


app = FastAPI()

# 설정
secrets_key = "129837190287"
expire_minutes = 60
ALGORITHM = "HS256"

# 토큰 생성
def create_jwt_token(sub: int, expires_minutes: int = expire_minutes) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expires_minutes)
    payload = {
        "sub": str(sub),
        "iat": int(now.timestamp()),
        "exp": int(expire.timestamp()),
        "type": "access"
    }
    token = encode(payload, secrets_key, algorithm=ALGORITHM)
    print("DEBUG payload:", payload)
    print("현재 서버 시간:", int(time.time()))
    return token

# 토큰 검증
def verify_jwt_token(token: str) -> dict:
    try:
        payload = decode(token, secrets_key, algorithms=[ALGORITHM])
        if not payload.get("sub"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="토큰에 유저 정보 없음.")
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="토큰 유효기간 만료됨")
    except InvalidTokenError as e:
        print("에러 : ", str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지 않은 토큰")

# 사용자 확인 의존성
def check_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization 헤더가 없거나 형식이 잘못됨")
    token = authorization.split(" ", 1)[1]
    payload = verify_jwt_token(token)
    return payload 

router = APIRouter(prefix="/root")


@router.get("/public")
def public():
    return {"msg": "public endpoint"}


@router.get("/protected")
def protected(payload: dict = Depends(check_token)):
    return {"msg": "protected", "sub": payload.get("sub")}


@router.post("/create_token")
def create_token(id: int):
    token = create_jwt_token(id)
    return {"access_token": token, "token_type": "bearer", "expires_in": expire_minutes * 60}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)