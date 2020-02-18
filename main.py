from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {
        'Hello': 'World'
    }

@app.get('/books/{book_id}')
def get_book(book_id: int, q: str=None):
    return {
        'book_id': book_id,
        'q': q
    }
