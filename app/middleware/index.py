async def log_requests(request, call_next):
    host, port = request.scope.get("server", ("", 0))
    print("--------------------------------------")
    print("Request received")
    print(f"Request: {request.method} {request.url}")
    print(f"Server: {host}:{port}")
    print("---------------------------------------")
    response = await call_next(request)

    return response
    