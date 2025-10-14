import base64

# base64 인코딩
def base64_encode(data: str | bytes) -> str:
    if isinstance(data, str):
        data = data.encode()
    elif not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")
    
    encoded_txt = base64.urlsafe_b64encode(data).decode().rstrip("=")
    # print(encoded_txt)
    return encoded_txt

if __name__=="__main__":
    base64_encode("aslkdfjalksdjf")


# base64 인코딩
def base64_decode(s: str) -> bytes:
    s = s + ("=" * (-len(s) % 4))
    return base64.urlsafe_b64decode(s)