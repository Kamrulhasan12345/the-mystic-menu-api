from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from app.deps import supabase, verify_jwt, verify_jwt_ret
from app.schemas.auth import User

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    try:
        response = supabase.auth.sign_up(jsonable_encoder(user))

        return response.session

    except Exception as e: 
        raise HTTPException(
            status_code=500, detail=f"Signup failed: {e}"
        )
    
@router.post("/signin")
async def signin(user: User):
    try:
        response = supabase.auth.sign_in_with_password(jsonable_encoder(user))

        return response.session

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Signin failed: {e}"
        ) 
    
@router.get("/me")
async def me(token=Depends(verify_jwt_ret)):
    try:
        response = supabase.auth.get_user(token)

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Getting your information failed: {e}"
        ) 