from pydantic import BaseModel, Field, ValidationError
from enum import Enum
from datetime import datetime

class ContactType(Enum):
    RADIO = "Radio",
    VISUAL = "visual",
    PHYSICAL = "phisycal",
    TELEPATHIC = "telepathic",


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: 