import fastapi
from sql_base.models import User
from resolvers import check_login

user_router = fastapi.APIRouter()


@user_router.get("/")
def not_login():
    return {"Message": "Login in system"}


@user_router.get("/login")
def check_login_1(user: User):
    post_id = check_login(user)
    if post_id:
        return {"code": 200, "message": "Login correct", "post_id": post_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again", "post_id": None}
