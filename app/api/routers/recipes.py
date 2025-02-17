from fastapi import APIRouter, Depends, HTTPException
from app.ai_deps import generate_description, generate_recipe
from app.deps import verify_jwt, supabase
from app.schemas.recipes import RecipeIn, Recipe

router = APIRouter()

@router.get("/", tags=['recipes'])
async def get_recipes(user=Depends(verify_jwt)):
    try:
        response = supabase.table("recipes").select("*").eq("user_id", user.user.id).execute()

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Getting all recipes failed: {e}"
        )


@router.post("/", tags=['recipes'])
async def add_recipes(recipe: RecipeIn, user=Depends(verify_jwt)):
    try:
        response = supabase.table("recipes").insert({
            "user_id": user.user.id,
            "name": recipe.name,
            "type": recipe.type,
            "description": await generate_description(recipe.name, recipe.type)
        }).execute()

        return response

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=500, detail=f"Adding recipes failed: {e}"
        )

@router.get("/{id}", tags=['recipes'])
async def get_recipe(id: str, user=Depends(verify_jwt)):
    try:
        response = supabase.table("recipes").select("*").eq("user_id", user.user.id).eq("id", id).execute()

        return response

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Getting all recipes failed: {e}"
        )

@router.delete("/{id}", tags=['recipes'])
async def delete_recipe(id: str, user=Depends(verify_jwt)):
    try:
        response = supabase.table("recipes").delete().eq("user_id", user.user.id).eq("id", id).execute()

        return response
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Deleting recipes failed: {e}"
        )

@router.post("/random", tags=['recipes'])
async def create_random(user=Depends(verify_jwt)):
    try:
        recipe: Recipe = await generate_recipe()
        print(recipe)
        response = supabase.table("recipes").insert({
            "user_id": user.user.id,
            "name": recipe['name'],
            "type": recipe['type'],
            "description": recipe['description']
        }).execute()

        return response
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=500, detail=f"Adding recipes failed: {e}"
        )