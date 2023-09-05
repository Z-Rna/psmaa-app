from pydantic import BaseModel
from .Criterion import Criterion
from .Preference import Preference

class DataSMAA2(BaseModel):
    criList: Criterion
    preference: Preference