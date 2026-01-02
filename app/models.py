from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    # ADD THIS LINE:
    id = Column(Integer, primary_key=True, index=True) 
    
    title = Column(String)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)