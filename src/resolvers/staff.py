from sql_base import models
from sql_base import base_worker


def create_staff(staff: models.Staff) -> int:
    new_id = base_worker.execute("INSERT INTO staff(user_id, post_id, name, surname, date_birth) "
                                 "VALUES (?, ?, ?, ?, ?) "
                                 "RETURNING id",
                                 (staff.user_id, staff.post_id, staff.name, staff.surname, staff.date_birth))
    return new_id


def get_staff(staff: models.StaffSearch):
    first_row = True
    query = "SELECT id, user_id, post_id, name, surname, date_birth FROM staff "
    for key, value in staff.__dict__.items():
        if value is not None:
            if not first_row:
                query += "AND "
            else:
                query += "WHERE "
            query += f"{key} = \"{value}\" "
            first_row = False
    get_id = base_worker.execute(query=query, many=True)
    return get_id
