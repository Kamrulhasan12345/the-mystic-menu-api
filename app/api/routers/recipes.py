from fastapi import APIRouter, Depends

from app.deps import verify_jwt

router = APIRouter()

@router.get("/")
async def all_recipes(user=Depends(verify_jwt)):
    return

@router.get("/random")
async def random(user=Depends(verify_jwt)):
    return

@router.post("/custom")
async def custom(user=Depends(verify_jwt)):
    return

@router.get("/:id")
async def single_recipes(id: str, user=Depends(verify_jwt)):
    return

@router.get("/image-gen")
async def image_gen(id: str, user=Depends(verify_jwt)):
    return