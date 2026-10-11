from app.core.logging import logger

async def log_requests(request, call_next):
    host, port = request.scope.get("server", ("", 0))
    logger.info("--------------------------------------")
    logger.info("Request received")
    logger.info(f"Request: {request.method} {request.url}")
    logger.info(f"Server: {host}:{port}")
    logger.info("---------------------------------------")
    response = await call_next(request)

    return response
    