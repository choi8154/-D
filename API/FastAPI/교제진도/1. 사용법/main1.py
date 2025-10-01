from fastapi import FastAPI

app = FastAPI() #FastAPI의 인스턴스 생성

@app.get("/") #누군가 post요청을 보내면 밑의 함수를 통해 응답을 만들어냄.
def read_root():
    return {"massage": 'Hello, World!'}



#?실행 방법
# Uvicorn : ASGI 지원 프레임워크
# uvicorn fast:app --reload : 비동기 처리를 위하여 uvicorn으로 서버를 염.

#?문서화 툴 사용법
# 문서화 툴 : 
    #- /docs : Swagger UI. OAuth2 지원, 플러그인이나 추가 설정으로 UI변경 가능
    #- /redoc : 리독

#?팁
# "/"를 요청을 보내면 def가 정의 되어 있기때문에 응답을 하지만 
# "/asldkfj" 이런식으로 함수가 정의되지 않은 요청을 보내면 응답이 없는것임