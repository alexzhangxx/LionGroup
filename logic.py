
def login(user_id, password):
    user = find_user(user_id)
    if user is not None and user['password'] == password:
        return user
    else:
        return None