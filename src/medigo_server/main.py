import uvicorn
from fastapi import FastAPI
from medigo_server.models import ResponseModel

app = FastAPI()

# app.include_router()

@app.get("/health")
async def root() -> ResponseModel:
    return ResponseModel(success=True, message="Healthy")

def main() -> None:
    uvicorn.run("medigo_server.main:app", host="0.0.0.0",port=8000,reload=True)

if __name__ == " __main__":
    main()