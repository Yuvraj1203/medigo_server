from medigo_server.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4, UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Category_Model(Base):
    __tablename__ = "categories"

    id:Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)