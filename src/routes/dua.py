from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models import Dua
from src.schema import DuaCreate
from src.database import get_db

router = APIRouter()

@router.post("/")
def create_dua(dua: DuaCreate, db: Session = Depends(get_db)):
    db_dua = Dua(title=dua.title, content=dua.content, user_id=1)  
    db.add(db_dua)
    db.commit()
    db.refresh(db_dua)
    return db_dua
