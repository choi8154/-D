import json
from datetime import datetime, timedelta
from base64_encode import base64_encode

header = {"alg":"HS256", "typ":"JWT"}

result = json.dumps(header, separators=(',', ':'))

print(type(header))
print(type(result))

# =============base64 hash test================
sub = "choi"
name = "choiguen"
iat = datetime.utcnow()
exp = str(iat + timedelta(minutes=60))

header = {"alg": "HS256", "typ": "JWT"}
payload = {"sub": sub, "name":name, "exp":exp}

header_b64 = base64_encode(json.dumps(header,separators=(",",":")))
payload_b64 = base64_encode(json.dumps(payload, separators=(",",":")))

# 디버깅
print("="*50)
print("header_b64 : ", header_b64, "type : ", type(header_b64))
print("header_b64 : ", payload_b64, "type : ", type(payload_b64))
print("="*50)

# =============HMAC test================
import hmac
import hashlib

msg = b"Hello, world!"
print(hashlib.sha256(msg).hexdigest())

secret_key = b"alskdjf123"
print(hmac.new(secret_key,msg,hashlib.sha256).hexdigest())