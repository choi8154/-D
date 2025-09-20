#API란?
- Application Programming Interface.
- 하나의 프로그램에서 다른 프로그램으로 데이터를 주고받기 위한 방법.
- 그 방법은 코드를 짜서 만드는거임. 한마디로 메뉴판을 만드는 것

식당 메뉴판임
1. 파스타
2. 피자
3. 식전빵

```python
from fastapi import FastAPI
app = FastAPI()
app.get('/요청!!/') #해당 url로 get요청을 하면!
def func(): #아래 함수를 실행시켜
    return "옛다 응답니다." #요청에 응답을 보냄
```
>(GET요청)comic.naver.com/webtoon/detail?id=318995  
  ^                    ^                 ^  
 요청 방식        무슨 자료를 요청할지   요청에 필요한 추가정보
(method)          (endpoint)      (내 아이디, 이름, 몇화보고 싶은지 이런거)

REST API 원칙: 웹의 경우 이 원칙에 따라 작성하면 좋음

주소창 : API 요청 코드짜는 곳임(GET요청가능)
- 보통 클릭하면 자동으로 API를 요청함.

# public/private/partner API
- public API : 누구나 사용가능한 공개 API
- private API : 사내에서 몰래쓰는 API
- partner API : 미리 정해둔 놈만 쓰는 API

