from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    return 'Welcome to Test-API'


@app.get('/new_page')
async def new_page():
    return 'Welcome to New Page'


@app.get('/page/{page_no}')
async def page(page_no: int):
    return f'Page No. {page_no}'
