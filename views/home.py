import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()


@router.get('/favicon.io')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
    # return templates.TemplateResponse('index.html', {'request': request})


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
    # return templates.TemplateResponse('index.html', {'request': request, 'other': [1, 2, 3]})


