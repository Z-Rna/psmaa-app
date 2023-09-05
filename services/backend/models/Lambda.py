from pydantic import BaseModel

class Lambda(BaseModel):
    min: float | int
    max: float | int