from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


async def exception_handler(request: Request, exc: HTTPException):
    print(f"Exception handled: {exc.status_code} - {exc.detail} for {request.method} {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )