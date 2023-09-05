from pydantic import BaseModel
from .Criterion import Criterion
from .Preference import Preference
from .Lambda import Lambda

class DataSMAATri(BaseModel):
    criList: Criterion
    preference: Preference
    lambda_value: Lambda