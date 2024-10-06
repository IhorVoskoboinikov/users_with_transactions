import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqladmin import Admin

from database import engine
from settings import settings
from transactions.views import TransactionAdmin
from users.router import router as user_router
from transactions.router import router as transactions_router
from users.views import UserAdmin

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

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(TransactionAdmin)


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
    uvicorn.run("main:app", host=settings.FAST_APP_HOST, port=settings.FAST_APP_PORT)
