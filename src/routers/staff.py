import fastapi
from resolvers import create_staff, get_staff
from sql_base import models
staff_router = fastapi.APIRouter()


@staff_router.get("/")
def start_page():
    return f"Hello friend"


@staff_router.get("/staff")
def get_staffs(staff: models.StaffSearch):
    staff_id = get_staff(staff)
    return staff_id


@staff_router.post("/staff")
def new_staff(staff: models.Staff):
    new_id = create_staff(staff)
    return f"{{code: 201, id: {new_id}}}"
