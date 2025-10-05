from functools import wraps

CURRENT_ROLE: str = "user"


def require_role(*allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if CURRENT_ROLE in allowed_roles:
                return func(*args, **kwargs)
            else:
                raise RuntimeError("RuntimeError")
        return wrapper
    return decorator


@require_role("admin", "moderator")
def drop_table():
    return "dropped"


def main():
    global CURRENT_ROLE
    print(drop_table())  # RuntimeError

    CURRENT_ROLE = "admin"
    print(drop_table())  # "dropped"


if __name__ == "__main__":
    main()
