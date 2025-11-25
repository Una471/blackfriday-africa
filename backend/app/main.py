from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router

app = FastAPI(
    title="BlackFriday CSV API",
    description="API serving products directly from CSV instead of a database.",
    version="1.0.0"
)

# --- CORS ---
origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://blackfriday-africa.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "BlackFriday CSV API Live"}

# Use router (which you will modify next)
app.include_router(router)
