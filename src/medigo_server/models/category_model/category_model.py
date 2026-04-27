from medigo_server.database import Base
from sqlalchemy import Column, String, Boolean

class Category_Model(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)