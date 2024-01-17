from typing import Union
import uvicorn
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/blog/unpublished')
def unpublished():
    return {'Data':'This is unpublished Data'}

@app.get("/blog")
def read_root(item = 10, published:bool = True , sort:Optional[str] = 'ok'):
    if published:
        return {"Hello": f"World {item} and {sort}"}
    else:
        return {'ok':f'{item} is not published yet'}
    return {'ok': f'{item} is not published yet but will soon do it'}



@app.get('/blog/{id}')
def read_item(id:int):
    return {"item_id": id}

@app.get('/blog/{id}/comment')
def read_item(id:int,limit = 78):
    return limit
    return {"item_id": {'1st cmnt','2nd cmnt'}}