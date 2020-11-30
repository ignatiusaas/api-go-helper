from pymongo import MongoClient
from pprint import pprint
import json
from bson import json_util

class Database():
    def __init__(self):
        client = MongoClient("mongodb+srv://dbAdmin:admin123@go1.ovymg.mongodb.net/gotukang?retryWrites=true&w=majority")
        self.Tukang=client.gotukang.tukang
        self.User=client.gotukang.user
        self.Review=client.gotukang.review
        self.Order=client.gotukang.order
    
    def addTukang(self,data):
        self.Tukang.insert_one(data)
        return("Tukang added")

    def listTukang(self):
        tukanglist = self.Tukang.find()
        listkosong = []
        for c in tukanglist:
            calon = {}
            keys = c.keys()
            for k in keys:
                if(k != '_id'):
                    calon[k] = c[k]
            listkosong.append(calon)
        print(listkosong)
        return(listkosong)

    def findTukang(self,data):
        result = self.Tukang.find_one(data)
        listkosong = []
        keys = result.keys()
        calon = {}
        for k in keys:
            if(k != '_id'):
                calon[k] = result[k]
        listkosong.append(calon)
        print(listkosong)
        return(listkosong)

    def delTukang(self,data):
        self.Tukang.delete_one(data)
        return("Tukang deleted")
    
    def clearTukang(self):
        self.Tukang.delete_many({})
        return("Tukang cleared")

    def addUser(self,data):
        self.User.insert_one(data)
        return("User added")

    def listUser(self):
        userlist = self.User.find()
        listkosong = []
        for c in userlist:
            calon = {}
            keys = c.keys()
            for k in keys:
                if(k != '_id'):
                    calon[k] = c[k]
            listkosong.append(calon)
        print(listkosong)
        return(listkosong)

    def findUser(self,data):
        result = self.User.find_one(data)
        listkosong = []
        keys = result.keys()
        calon = {}
        for k in keys:
            if(k != '_id'):
                calon[k] = result[k]
        listkosong.append(calon)
        print(listkosong)
        return(listkosong)
        
    def delUser(self,data):
        self.User.delete_one(data)
        return("User deleted")
    
    def clearUser(self):
        self.User.delete_many({})
        return("User cleared")
    
    def addReview(self,data):
        self.Review.insert_one(data)
        return("Review added")
        
    def findReview(self,data):
        reviewlist = self.Review.find(data)
        listkosong = []
        for c in reviewlist:
            calon = {}
            keys = c.keys()
            for k in keys:
                if(k != '_id' and k != 'usernameTk'):
                    calon[k] = c[k]
            listkosong.append(calon)
        print(listkosong)
        return(listkosong)

    def addOrder(self,data):
        self.Order.insert_one(data)
        return("Order added")

    def findOrder(self,data):
        orderlist = self.Order.find(data)
        listkosong = []
        for c in orderlist:
            calon = {}
            keys = c.keys()
            for k in keys:
                if(k != '_id' and k != 'usernameTk'):
                    calon[k] = c[k]
            listkosong.append(calon)
        print(listkosong)
        return(listkosong)