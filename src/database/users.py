from sqlalchemy import String, Column, UUID

from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    email = Column(String(64))
    password = Column(String(64))

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, "
                f"first_name={self.first_name!r}, "
                f"last_name={self.last_name!r}, "
                f"email={self.email!r}, "
                f"first_name={self.password!r})")
