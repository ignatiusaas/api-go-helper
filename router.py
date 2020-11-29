from fastapi import HTTPException, Depends, Request
from fastapi import APIRouter
from model import *
from database import Database

router = APIRouter()

@router.post("/tukang/add")
def addTk(tk: Tukang):
    return{Database().addTukang(tk.dict())}

@router.get("/tukang/list")
def listTk():
    return{"list": Database().listTukang()}

@router.get("/tukang/find/username")
def findTk(tk: TukangSUsername):
    return{"result": Database().findTukang(tk.dict())}
@router.get("/tukang/find/specialization")
def findTk(tk: TukangSSpecialization):
    return{"result": Database().findTukang(tk.dict())}
@router.get("/tukang/find/location")
def findTk(tk: TukangSLocation):
    return{"result": Database().findTukang(tk.dict())}
@router.get("/tukang/find/review")
def findTk(tk: TukangSReview):
    return{"result": Database().findTukang(tk.dict())}

@router.get("/tukang/delete/username")
def delTk(tk: TukangSUsername):
    return{"result": Database().findTukang(tk.dict())}
@router.get("/tukang/delete/specialization")
def delTk(tk: TukangSSpecialization):
    return{"result": Database().findTukang(tk.dict())}
@router.get("/tukang/delete/location")
def delTk(tk: TukangSLocation):
    return{"result": Database().findTukang(tk.dict())}
@router.get("/tukang/delete/review")
def delTk(tk: TukangSReview):
    return{"result": Database().findTukang(tk.dict())}

@router.post("/tukang/clear")
def clearTk():
    return{Database().clearTukang()}

@router.post("/user/add")
def addUs(us: User):
    return{Database().addUser(us.dict())}
    
@router.get("/user/list")
def listUs():
    return{"list": Database().listUser()}

@router.get("/user/find/username")
def findUs(us: TukangSUsername):
    return{"result": Database().findUser(us.dict())}
@router.get("/user/find/location")
def findUs(us: TukangSLocation):
    return{"result": Database().findUser(us.dict())}

@router.get("/user/delete/username")
def delUs(us: TukangSUsername):
    return{"result": Database().delUser(us.dict())}
@router.get("/user/delete/location")
def delUs(us: TukangSLocation):
    return{"result": Database().delUser(us.dict())}

@router.post("/user/clear")
def clearUs():
    return{Database().clearUser()}

@router.post("/review/add")
def addRv(rv: Review):
    return{Database().addReview(rv.dict())}

@router.get("/review/find")
def findRv(rv: ReviewSUsername):
    return{"reviews": Database().findReview(rv.dict())}

@router.post("/order/add")
def addOr(orda: Order):
    return{Database().addOrder(orda.dict())}