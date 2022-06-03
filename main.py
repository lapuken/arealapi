import fastapi
import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

api = fastapi.FastAPI()
templates = Jinja2Templates('templates')
api.mount('/static', StaticFiles(directory='static'), name='static')


@api.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
    # return templates.TemplateResponse('index.html', {'request': request, 'other': [1, 2, 3]})


if __name__ == '__main__':
    uvicorn.run(api, port=8008, host="127.0.0.1")
