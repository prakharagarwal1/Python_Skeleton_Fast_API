from fastapi import FastAPI, HTTPException,Depends,APIRouter
router = APIRouter()



def get_settings():
    return {
        "environment": "development"
    }

@router.get("/config")
async def config(settings=Depends(get_settings)):
    return settings