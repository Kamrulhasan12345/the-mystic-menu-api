from typing import Annotated
from pydantic import BaseModel, StringConstraints, field_validator
from uuid import UUID


class RecipeIn (BaseModel):
    name: str
    type: Annotated[str, StringConstraints(min_length=1)] = "Unknown"

class Recipe (RecipeIn):
    description: str

class RecipeInDB (Recipe):
    user_id: UUID