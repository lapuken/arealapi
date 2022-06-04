import fastapi
import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from api import weather_api
from views import home

api = fastapi.FastAPI()

api.mount('/static', StaticFiles(directory='static'), name='static')
api.include_router(home.router)
api.include_router(weather_api.router)


if __name__ == '__main__':
    uvicorn.run(api, port=8008, host="127.0.0.1")
