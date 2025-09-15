def require_login(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if not user or not user.get("is_authenticated"):
            return "Access Denied"
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_profile(user=None):
    return f"Welcome {user['name']}!"

print(view_profile(user={"name": "Archana", "is_authenticated": True}))
