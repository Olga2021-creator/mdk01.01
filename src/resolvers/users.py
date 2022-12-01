from sql_base import models
from sql_base import base_worker


def check_login(user: models.User) -> int:
    query = """SELECT post_id FROM staff S
                INNER JOIN users U on S.user_id = U.id
                WHERE U.login = ? AND U.password = ?"""
    get_id = base_worker.execute(query, (user.login, user.password), many=False)
    return get_id
