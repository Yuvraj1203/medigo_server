import uvicorn
from fastapi import FastAPI
from medigo_server.schemas import ResponseModel
from medigo_server.routers import router
from fastapi.middleware.cors import CORSMiddleware
from medigo_server.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

# Add CORS middleware **here**
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use "*" if needed during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def root() -> ResponseModel:
    return ResponseModel(success=True, message=f"Healthy")


def main() -> None:
    uvicorn.run("medigo_server.main:app", host="0.0.0.0",port=8000,reload=True)

if __name__ == " __main__":
    main()