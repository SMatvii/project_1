from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(engine)
LocalSession = scoped_session(engine)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


def up():
    Base.metadata.create_all(engine)

def down():
    Base.metadata.drop_all(engine)

from .models import Books

down()
up()