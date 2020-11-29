from pydantic import BaseModel
from typing import Optional

class Tukang(BaseModel):
    username: str
    specialization: str
    location: str
    review: Optional[float] = "0"

############TUKANG SEARCH############
class TukangSUsername(BaseModel):
    username: str
class TukangSSpecialization(BaseModel):
    specialization: str
class TukangSLocation(BaseModel):
    location: str
class TukangSReview(BaseModel):
    review: float
#####################################

class User(BaseModel):
    username: str
    location: str

#############USER SEARCH#############
class UserSUsername(BaseModel):
    username: str
class UserSLocation(BaseModel):
    location: str
#####################################

class Review(BaseModel):
    usernameTk: str
    star: float
    comment: Optional[str] = ""
    usernameUs: str

class ReviewSUsername(BaseModel):
    usernameTk: str

class Order(BaseModel):
    usernameUs: str
    usernameTk: str
    location: str
