from typing import Union
import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    pub: Optional[bool] = True

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f"{blog.title} is title of the blog"}

@app.get("/blog")
def read_root(item=10, published: bool = True, sort: Optional[str] = 'ok'):
    if published:
        return {"Hello": f"World {item} and {sort}"}
    else:
        return {'ok': f'{item} is not published yet'}
    # return {'ok': f'{item} is not published yet but will soon do it'}


@app.get('/blog/{ids}')
def read_item(ids: int):
    return {"item_id": ids}


@app.get('/blog/{id}/comment')
def read_item(id: int, limit=78):
    return limit
