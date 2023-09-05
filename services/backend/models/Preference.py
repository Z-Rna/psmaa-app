from pydantic import BaseModel

class Preference(BaseModel):
    isEditing: bool
    name: str
    preferenceArray: list