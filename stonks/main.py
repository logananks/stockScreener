import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

class StockRequest(BaseModel):
    symbol: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
@app.get("/")
def home(request: Request):
    """
    displays the stock screener dashboard / homepage
    """
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/stock")
def create_stock(stock_request: StockRequest):
    """
    created a stock and stores it in the database
    """
    return {
        "code": "success",
        "message": "stock created"
    }

