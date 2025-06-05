# 假設說回傳的error如下

mock_error_response = {
    "status": {
        "code": 500,
        "msg": "Validation failed."
    },
    "data": {
        "errors": "price: The price must be numeric"
    }
}

error_msg = mock_error_response["data"]["errors"]
print("Errors内容:", error_msg)