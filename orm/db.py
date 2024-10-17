from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from contextlib import contextmanager


engine = create_engine(
    url=settings.DATABASE_URL(),
    echo=False
)

Session = sessionmaker(bind=engine)

@contextmanager
def set_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()

