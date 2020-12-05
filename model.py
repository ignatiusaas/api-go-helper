from pydantic import BaseModel
from typing import Optional

class Tukang(BaseModel):
    username: str
    specialization: str
    location: str
    review: Optional[float] = "0"

class UpdateTukang(BaseModel):
    username: str
    specialization: Optional[str]
    location: Optional[str]
    review: Optional[float]

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

class UpdateUser(BaseModel):
    username: Optional[str]
    location: Optional[str]

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

class UpdateReview(BaseModel):
    usernameTk: str
    star: Optional[float]
    comment: Optional[str]
    usernameUs: str

class ReviewSUsername(BaseModel):
    usernameTk: str

class Order(BaseModel):
    usernameUs: str
    usernameTk: str
    location: str

class UpdateOrder(BaseModel):
    usernameUs: str
    usernameTk: str
    location: Optional[str]

class OrderSUsername(BaseModel):
    usernameTk: str
