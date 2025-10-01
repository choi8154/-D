from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ?중첩된 모델
class Image(BaseModel):
    url : str
    name : str

class Item(BaseModel):
    name : str
    description : str
    image : Image

@app.post('/items/')
def create_items(item:Item):
    return {"item":item.dict()}


#?중첩된 모델이란?
# 한 모델(BaseModel) 안에 다른 모델을 속성으로 포함하는 것.
# 이러면 해당 모델을 다른속성에서 똑같이 사용할 수 있고 수정이 편함.

# ?curl Test
'''
curl -X POST "http://127.0.0.1:8000/items/" \
-H "accept:application/json" \
-H "Content-Type:application/json" \
-d '{"name":"smartphone","description":"latest model","image":{"url":"http://example.com/image.jpg", "name":"front_view"}}'
'''
