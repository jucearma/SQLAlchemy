from datetime import datetime
from src.database import Session, init_db
from src.models.Book import Book

if __name__ == '__main__':
    init_db()
    book = Book(
        title='Test Book',
        author='Peter Mejia',
        pages=360,
        published=datetime(2020, 1, 27)
    )
    s = Session()
    try:
        s.add(book)
    except Exception:
        s.rollback()
        raise
    else:
        s.commit()
    finally:
        s.close()
