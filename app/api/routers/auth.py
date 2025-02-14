from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.deps import supabase
from app.schemas.auth import User

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    try:
        response = supabase.auth.sign_up(jsonable_encoder(user))

        return response.data 

    except Exception as e: 
        raise HTTPException(
            status_code=500, detail=f"Signup failed: {e}"
        )