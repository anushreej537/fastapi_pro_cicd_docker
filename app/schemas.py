from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# This is used when creating a task (user doesn't provide ID)
class TaskCreate(TaskBase):
    pass

# This is used when sending data back (includes the ID from the database)
class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True # This allows Pydantic to work with database objects