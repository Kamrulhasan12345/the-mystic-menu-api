from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import auth, recipes

description = """
The Mystic Menu API empowers culinary creativity. It provides the tools for developers to build innovative recipe creation and management applications.  Key features include:

Recipe Creation: Enable users to easily create and store their own recipes, including ingredients, instructions, and images.
Customization: Support personalized recipe variations, dietary adjustments, and ingredient substitutions.
Organization: Facilitate recipe organization through categories, tags, collections, and meal planning features.
Sharing: Allow users to share their culinary creations with friends, family, or the wider community.
Integration: Seamlessly integrate recipe management into existing food-related apps or platforms.
"""

app = FastAPI(
    title="The Mystic Menu API",
    description=description,
    summary="The Mystic Menu API empowers developers to create innovative recipe management applications, enabling users to create, customize, organize, share, and integrate recipes.",
    version="0.0.1",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(recipes.router, prefix="/recipes")

@app.get("/")
async def root():
    return {"detail": "Go to /docs to get started!"}