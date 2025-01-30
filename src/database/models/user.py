import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from general import db


class User(db.Model):
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[bytes]
