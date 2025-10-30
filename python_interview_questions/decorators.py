def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_execution
def add(a, b):
    return a + b

print(add(3, 5))

def to_uppercase(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@to_uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated", False):
            raise PermissionError("Access denied: user not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def get_user_data(user):
    return f"Data for {user['name']}"

# secure_function = require_auth(get_user_data)
# print(secure_function({"name": "Bob", "is_authenticated": False}))

# Example
print(get_user_data({"name": "Alice", "is_authenticated": True}))
print(get_user_data({"name": "Bob", "is_authenticated": False}))  # raises error
