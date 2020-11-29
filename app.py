from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from router import *

app=FastAPI()
app.include_router(router)

@app.get("/testing")
def testing():
	return{"Hello": "world"}