from medigo_server.database import Base
from medigo_server.common.enums import MedicineType
from sqlalchemy import Column, String, Boolean, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4

medicine_type: Mapped[MedicineType] = mapped_column(
    Enum(MedicineType),
    nullable=False
)

image_url: Mapped[list[str] | None] = mapped_column(
    ARRAY(String),
    nullable=True
)

class Product_Model(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()), index=True)
    name= Column(String, nullable=False)
    generic_name= Column(String, nullable=True)
    brand = Column(String, nullable=True)
    category_id = Column(String,ForeignKey("categories.id"), nullable=False)
    requires_prescription = Column(Boolean, default=True)
    description = Column(String, nullable=True)
    manufacturer = Column(String, nullable=True)
    medicine_type = medicine_type
    image_url = image_url
    is_active = Column(Boolean, default=True)