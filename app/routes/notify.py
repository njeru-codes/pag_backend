from fastapi import APIRouter,Depends, HTTPException
from app.schemas import NewNotification
from motor.motor_asyncio  import AsyncIOMotorDatabase
from app.database import get_db

router = APIRouter()


@router.get('/notify')
async def get_notification(db: AsyncIOMotorDatabase = Depends(get_db)):
    pass

@router.post('/notify')
async def new_notification(notify:NewNotification, db: AsyncIOMotorDatabase = Depends(get_db)):
    pass
