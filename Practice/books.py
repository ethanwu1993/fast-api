from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
]


@app.get("/books/all-books")
async def read_all_books():
    return BOOKS


# @app.get("/books/{param}")
# async def read_books(param):
#     return {param: param}


# @app.get("/books/{book_title}")
# async def read_books(book_title: str):
#     for book in BOOKS:
#         if book.get('title').casefold() == book_title.casefold():
#             return book
#
#
# @app.get('/books/')
# async def read_category_by_query(category: str):
#     books_to_return = []
#
#     for book in BOOKS:
#         if book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
#
#     return books_to_return
#
#
# @app.get('/books/{book_author}/')
# async def read_author_category_by_query(book_author: str, category: str):
#     books_to_return = []
#
#     for book in BOOKS:
#         if book.get('author').casefold() == book_author.casefold() \
#                 and book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
#
#     return books_to_return


@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put('/books/update_book')
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book


@app.delete("/books/delete/{book_title}")
async def delete(book_title: str):
    for i in range(len(BOOKS)):
        if book_title.casefold() == BOOKS[i].get('title').casefold():
            BOOKS.pop(i)
            break


# Path Param
@app.get('/books/{book_author}')
async def get_all_books_from_author_path(book_author: str):
    all_books = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            all_books.append(book)

    return all_books


# query param
@app.get('/books/')
async def get_all_books_from_author_query(book_author: str):
    all_books = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            all_books.append(book)

    return all_books
