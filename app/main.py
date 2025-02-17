from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import auth, recipes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(recipes.router, prefix="/recipes")