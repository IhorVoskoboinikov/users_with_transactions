RESPONSES_USERS = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": [
                    {
                        "user_name": "Test",
                        "id": 1,
                        "transactions": [
                            {
                                "user_id": 1,
                                "transaction_type": "deposit",
                                "amount": 500,
                                "id": 1,
                            }
                        ],
                    },
                    {
                        "user_name": "AnotherTest",
                        "id": 2,
                        "transactions": [
                            {
                                "user_id": 2,
                                "transaction_type": "withdrawal",
                                "amount": 300,
                                "id": 2,
                            }
                        ],
                    },
                ]
            }
        },
    }
}
RESPONSES_GER_USER = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "example": {
                    "user_name": "Test User",
                    "id": 1,
                    "transactions": [
                        {
                            "create_at": "2024-10-07T19:13:58.996203",
                            "id": 1,
                            "user_id": 1,
                            "transaction_type": "transfer",
                            "amount": 100.00,
                        }
                    ],
                }
            }
        },
    },
    404: {
        "description": "User not found",
        "content": {"application/json": {"example": {"detail": "User not found"}}},
    },
    422: {
        "description": "Validation Error",
        "content": {"application/json": {"example": {"detail": "Invalid input data"}}},
    },
}
RESPONSES_USER_CREATE = {
    200: {
        "description": "Success",
        "content": {"application/json": {"example": {"ID": 1}}},
    },
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {"detail": "User with this name already exists"}
            }
        },
    },
    422: {
        "description": "Validation Error",
        "content": {"application/json": {"example": {"detail": "Invalid input data"}}},
    },
}
RESPONSES_TRANSACTION = {
    200: {
        "description": "Successful operation",
        "content": {
            "application/json": {
                "example": {
                    "id": 1,
                    "user_id": 1,
                    "creation_date": "2024-10-07T20:12:42.797690",
                    "transaction_amount": 500.0,
                    "transaction_type": "deposit | withdrawal | transfer",
                }
            }
        },
    },
    404: {
        "description": "User with ID '1' doesn't exist in db",
        "content": {
            "application/json": {
                "example": {"detail": "User with ID '1' doesn't exist in db"}
            }
        },
    },
    422: {
        "description": "Validation Error",
        "content": {"application/json": {"example": {"detail": "Invalid input data"}}},
    },
}
