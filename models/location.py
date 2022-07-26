from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    city: str = 'Boston'
    state: Optional[str] = "MA"
    country: Optional[str] = "USA"
