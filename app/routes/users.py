from fastapi import APIRouter,Depends, HTTPException
from app.schemas import NewUser, LoginUser
from app.database import get_db
from motor.motor_asyncio  import AsyncIOMotorDatabase
from datetime import datetime
from app.utils import hash_function, verify_password
from app.auth import create_access_token, get_current_user

router = APIRouter()


@router.post('/register')
async def create_user(new_user: NewUser, db: AsyncIOMotorDatabase = Depends(get_db)):

    existing_user = await db.users.find_one({"email": new_user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail=f"user with email {new_user.email} exists")

    new_user_dict = new_user.dict()
    new_user_dict['password'] = hash_function( new_user.password )
    new_user_dict['created_at'] = datetime.utcnow().isoformat()  
    new_user_dict['disabled'] = False 
    new_user_dict['email_verified'] = False  

    
    result = await db.users.insert_one(new_user_dict)
    
    
    if result.inserted_id is None:
        raise HTTPException(status_code=500, detail="User not added to DB")

    user_db ={
        "user_id": str(result.inserted_id),
        "email": new_user_dict['email']
    }
    return user_db 


@router.post('/login')
async def login_user( login_user: LoginUser, db: AsyncIOMotorDatabase = Depends(get_db)):
    existing_user = await db.users.find_one({"email": login_user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="invalid user or password")

    if not verify_password(login_user.password , existing_user['password']):
        raise HTTPException(status_code=400, detail="invalid user or password")

    access_token = create_access_token(data={'user_id': str(existing_user['_id'])})
    return   { "access_token": access_token, "token_type": "bearer" }

@router.get('/profile')
async def get_user_profile(db: AsyncIOMotorDatabase = Depends(get_db), user_id:str =Depends(get_current_user) ):
    return user_id
    