from functools import wraps
CURRENT_ROLE = "user"

def require_role(*allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_ROLE in allowed_roles:
                return func(*args, **kwargs)
            else: 
                raise RuntimeError
        return wrapper
    return decorator

@require_role("admin", "moderator")
def drop_table():
    return "dropped"

print(drop_table())  # RuntimeError

CURRENT_ROLE = "admin"
print(drop_table())  # "dropped"