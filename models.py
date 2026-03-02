from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    completed: bool = False
