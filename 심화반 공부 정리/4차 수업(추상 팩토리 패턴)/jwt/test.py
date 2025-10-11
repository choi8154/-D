# from datetime import datetime

# A = "2025-10-04 10:57:34.405537"
# A = datetime.fromisoformat(A)
# print(datetime.utcnow())
# print(A > datetime.utcnow())
A = False
if not A : 
    print(A)

class UserData:
    def __init__(self, token, id):
        self.token = token
        self.id = id

user = UserData("asdf", "Asdf")
print(user.id)
id.id