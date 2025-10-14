# jwt 구조

## 팁s
1. 
    - digest() : 바이너리(bytes)를 반환. (원시 바이트, 이걸로 서명하거나 바로 base64 인코딩함) -> 암호 서명, JWT 서명에 사용할 때
    - hexdigest() : 16진수 문자열(str)을 반환. (사람이 읽기 쉬운 형태, 로그/DB에 저장할 때 편함) -> 디버깅 하거나, db에 넣을 때

## jwt의 심장 HMAC
HMAC는 해시화된 코드에 secret_key를 같이 갈아넣어 마음대로 디코딩 할 수 없도록 만든 암호화 기법이다.
```py
import hmac
import hashlib

msg = b"Hello, world!"
print(hashlib.sha256(msg).hexdigest())
```
> 출력값 : 315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3
sha256은 단방향 인코딩이라 디코딩이 쉽지는 않다.
하지만 클라이언트가 능력이 있고 마음만 먹으면 디코딩이 가능하기에 중요한 정보를 담기에는 상당히 위험하다.
그렇기에 HMAC를 활용해 보안을 강화하는 것이다.
```py
import hmac
import hashlib

secret_key = b"alskdjf123"
print(hmac.new(secret_key,msg,hashlib.sha256).hexdigest())
```
> 출력값 : ff932b1810234e4153665132eb83de0cf6d32835acf0f55df805a5196aecbc10

하지만 이 또한 secrit_key를 도난당하면 위험하기에 secrit_key는 안전한 곳에 감추는게 정석이다.