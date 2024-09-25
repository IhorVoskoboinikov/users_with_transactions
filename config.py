import os
from dotenv import load_dotenv


def get_env_data(name: str) -> str:
    env_data = os.getenv(name)
    if env_data is None:
        load_dotenv()
        env_data = os.getenv(name)
    return env_data


FAST_APP_HOST = get_env_data("FAST_APP_HOST")
FAST_APP_PORT = int(get_env_data("FAST_APP_PORT"))

POSTGRES_USER = get_env_data("POSTGRES_USER")
POSTGRES_HOST = get_env_data("POSTGRES_HOST")
POSTGRES_PORT = int(get_env_data("POSTGRES_PORT"))
POSTGRES_PASSWORD = get_env_data("POSTGRES_PASSWORD")
POSTGRES_DB = get_env_data("POSTGRES_DB")


RESPONSES_USER = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": {
                    "user_id": 1,
                    "user_name": "john_doe",
                }
            }
        }
    },
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {
                    "detail": "User with this name already exists"
                }
            }
        }
    },
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "detail": "User not found"
                }
            }
        }
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Invalid input data"
                }
            }
        }
    },
}

RESPONSES_TRANSACTION = {
    200: {
        "description": "Successful operation",
        "content": {
            "application/json": {
                "example": {
                    "id": 6,
                    "user_id": 6,
                    "creation_date": "2024-09-25",
                    "transaction_amount": 500.0,
                    "transaction_type": "Test"
                }
            }
        }
    },
    404: {
        "description": "Not Found",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Transaction with ID '1' not found | User with ID '1'doesn't exist in db"
                }
            }
        }
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Invalid input data"
                }
            }
        }
    }
}
