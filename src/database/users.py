from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(64))

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, "
                f"first_name={self.first_name!r}, "
                f"last_name={self.last_name!r}, "
                f"email={self.email!r}, "
                f"first_name={self.password!r})")
