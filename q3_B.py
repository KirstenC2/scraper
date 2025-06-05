# 假設說回傳一下的error

mock_response = {
    "status": {
        "code": 500,
        "msg": "Validation failed."
    },
    "data": {
        "errors": "price: The price must be numeric"
    }
}

error_msg = mock_response["data"]["errors"]
print("Errors内容:", error_msg)