from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Local app imports
from .routes import router

app = FastAPI(
    title="BlackFriday.Africa API",
    description="API for BlackFriday.Africa MVP",
    version="0.1.0",
)

# CORS Middleware
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

# Include API routes
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the BlackFriday.Africa API"}
