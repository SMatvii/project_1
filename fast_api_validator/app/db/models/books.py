from .. import Base
from sqlalchemy.orm import Mapped, mapped_column


class Books(Base):
    __tablename__ = "task"

    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str]
    year: Mapped[int]
    genre: Mapped[str]
    isbn: Mapped[str]