from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import Base, engine
from src.routes import auth, dua
from sqlalchemy import text
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(dua.router, prefix="/duas", tags=["Duas"])

@app.get("/")
async def root():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(result.fetchall(), "result")
        
    return {"message": "Welcome to DUA API"}
