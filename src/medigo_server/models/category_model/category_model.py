from medigo_server.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4

class Category_Model(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()) ,index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)