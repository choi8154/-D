# app/main.py
from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import secrets
import jwt
from typing import List, Dict
from datetime import datetime, timedelta

# ------------- 가상의 DB (간단 예시) -------------
# 실제 환경에선 SQLAlchemy + 비밀번호 해시 사용 권장
db: List[Dict] = [{"id": "admin", "password": "pw"}]
# -------------------------------------------------

templates = Jinja2Templates(directory="app/templates")

app = FastAPI()
router = APIRouter(prefix="/homepage")

# JWT 설정
SECRET_KEY = secrets.token_urlsafe(32)  # 문자열형 비밀키
ALGORITHM = "HS256"
ACCESS_EXPIRE_MINUTES = 15

def create_access_token(subject: str, expires_minutes: int = ACCESS_EXPIRE_MINUTES) -> str:
    now = datetime.utcnow()
    payload = {
        "sub": str(subject),
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=expires_minutes)).timestamp()),
        "type": "access"
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ----------------- 미들웨어: 전역 토큰 검사 -----------------
# 화이트리스트 경로는 토큰 검사에서 제외 (로그인/회원가입/정적파일 등)
WHITELIST_PATHS = {
    "/homepage/",         # 로그인 페이지 (GET)
    "/homepage/signup",   # 회원가입
    "/openapi.json",
    "/docs",
    "/docs/oauth2-redirect"
}

@app.middleware("http")
async def token_check_middleware(request: Request, call_next):
    path = request.url.path
    # OPTIONS이나 화이트리스트는 검사 제외
    if request.method == "OPTIONS" or any(path.startswith(p) for p in WHITELIST_PATHS):
        return await call_next(request)

    # Authorization 헤더에서 Bearer 토큰 확인
    auth: str | None = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Missing Authorization Bearer token"})

    token = auth.split(" ", 1)[1]
    try:
        payload = verify_token(token)
        # 검사 통과하면 request.state에 사용자 정보 저장 (다음 라우트에서 사용 가능)
        request.state.user = payload
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    response = await call_next(request)
    return response
# --------------------------------------------------------

# ---------- Pydantic 스키마 (간단) ----------
class LoginSchema(BaseModel):
    id: str
    password: str

class SignupSchema(BaseModel):
    id: str
    password: str
# --------------------------------------------

# GET: 로그인 폼 렌더링
@router.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    # templates/login.html 이 존재해야 함
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

# POST: 로그인 처리 (JSON body로 받는 예시)
@router.post("/", response_class=JSONResponse)
def login_post(payload: LoginSchema):
    # 단순 예시: 실제론 해시 비교 사용
    user = next((u for u in db if u["id"] == payload.id and u["password"] == payload.password), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = create_access_token(subject=payload.id)
    # 응답으로 토큰 반환(프론트가 Authorization 헤더로 저장/사용) 또는 쿠키에 넣을 수 있음
    return {"access_token": access, "token_type": "bearer"}

# POST: 회원가입 (폼/JSON 가능) - HTMLResponse로 템플릿 반환 예시도 가능
@router.post("/signup", response_class=JSONResponse)
def signup(payload: SignupSchema):
    # id 중복 체크
    if any(u["id"] == payload.id for u in db):
        raise HTTPException(status_code=400, detail="id already exist")
    # 실제론 비밀번호 해시화 필요
    db.append({"id": payload.id, "password": payload.password})
    return {"msg": "user created", "id": payload.id}

# 보호된 라우트 예시: 미들웨어가 검사해서 request.state.user에 payload가 있음
@router.get("/me")
def me(request: Request):
    # 미들웨어에서 정상 검사되면 request.state.user가 채워짐
    user_payload = getattr(request.state, "user", None)
    if not user_payload:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"me": user_payload}

app.include_router(router)