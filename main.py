import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

import config
from users.router import router as user_router
from transactions.router import router as transactions_router

app = FastAPI(
    title="User and Transaction Management Service",
    version="1.0.0",
    description="A service for managing users and transactions",
    openapi_tags=[
        {
            "name": "Users",
            "description": "CRUD operations with Users"
        },
        {
            "name": "Transactions",
            "description": "CRUD operations with Transactions"
        }
    ]
)

app.include_router(user_router)
app.include_router(transactions_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request: Request, _exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "status": "Error",
            "detail": "Invalid input data"
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.FAST_APP_HOST, port=config.FAST_APP_PORT)
