import datetime
import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from general import db


class Saving(db.Model):
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    name: Mapped[str] = mapped_column()
    value: Mapped[float] = mapped_column()
    start_date: Mapped[datetime.date] = mapped_column()
    end_date: Mapped[datetime.date] = mapped_column(nullable=True)
    interval: Mapped[str] = mapped_column()
