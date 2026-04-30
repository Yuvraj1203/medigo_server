from medigo_server.database import Base
from medigo_server.common.enums import MedicineType
from sqlalchemy import String, ForeignKey, Enum, ARRAY
from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4, UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Product_Model(Base):
    __tablename__ = "products"

    id:Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),primary_key=True, default=uuid4)
    name= mapped_column(nullable=False)
    generic_name= mapped_column(nullable=True)
    brand = mapped_column(nullable=True)
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=False)
    requires_prescription: Mapped[bool] = mapped_column(default=True)
    description: Mapped[str] = mapped_column( nullable=True)
    manufacturer: Mapped[str] = mapped_column(nullable=True)
    medicine_type: Mapped[MedicineType] = mapped_column(Enum(MedicineType,name="medicine_type_enum"),nullable=False)
    image_url: Mapped[List[str] | None] = mapped_column(ARRAY(String),nullable=True) 
    is_active: Mapped[bool] = mapped_column(default=True)